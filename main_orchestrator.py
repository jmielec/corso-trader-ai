import os
import sys
import logging
import importlib # Added for dynamic imports
from dotenv import load_dotenv

# Add src directory to Python path
# This allows importing modules from src (e.g., src.utils.db_utils)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Now you can import from src.utils, src.modules, etc.
# Example (will be implemented later):
# from src.utils.logging_config import setup_logging
# from src.utils.db_utils import get_supabase_client

from src.utils.logging_config import setup_logging # Using the utility now
from src.utils.db_utils import get_supabase_client, query_module_registry, log_to_supabase

# Load environment variables from .env file
load_dotenv()

# Setup logging using the utility
# Note: setup_logging configures the root logger. Get specific logger for this module.
setup_logging()
logger = logging.getLogger(__name__)

def main():
    """Main entry point for the pipeline orchestrator."""
    logger.info("Starting Corso Trader AI pipeline orchestrator (v0.1 - Phase 0/1)")

    # --- Phase 0/1: Basic Setup ---
    # 1. Load Configuration (Environment Variables loaded above)
    # IMPORTANT: Ensure these env vars are set in Render:
    # SUPABASE_URL: Your project's API URL
    # SUPABASE_SERVICE_KEY: Your project's service_role key
    logger.info("Configuration loaded from environment.")

    # 2. Connect to Supabase
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("Failed to connect to Supabase. Check SUPABASE_URL/SUPABASE_SERVICE_KEY env vars. Exiting.")
        sys.exit(1)
    logger.info("Successfully connected to Supabase.")

    # 3. Initialize Context Dictionary
    context_dict = {}
    logger.info("Initialized empty context dictionary.")

    # 4. Query Module Registry for a specific module (Hardcoded for now)
    target_module_id = "hello_module_v1" # Hardcoded for initial test
    logger.info(f"Attempting to find module in registry: {target_module_id}")
    module_details = query_module_registry(supabase_client, target_module_id)

    if not module_details:
        logger.error(f"Module '{target_module_id}' not found or inactive in registry. Exiting.")
        # Log failure to Supabase Error_Log table
        log_to_supabase(supabase_client, 'Error_Log', {
            'module_id': 'orchestrator',
            'error_message': f"Module '{target_module_id}' not found or inactive in registry.",
            'stage': 'module_lookup'
        })
        sys.exit(1)

    # 5. Dynamically Import and Execute Module
    try:
        script_rel_path = module_details['script_path'] # e.g., src/modules/context/hello_module_v1.py
        function_name = module_details['function_name'] # e.g., run
        module_version = module_details['version']

        # Convert file path to Python module path
        # src/modules/context/hello_module_v1.py -> src.modules.context.hello_module_v1
        module_import_path = script_rel_path.replace('/', '.').replace('.py', '')

        logger.info(f"Loading module {target_module_id} v{module_version} from '{module_import_path}'...")

        # Dynamically import the module
        module = importlib.import_module(module_import_path)
        logger.info(f"Module '{module_import_path}' imported successfully.")

        # Get the function object from the imported module
        if not hasattr(module, function_name):
             raise AttributeError(f"Module {module_import_path} does not have function '{function_name}'")
        run_function = getattr(module, function_name)

        logger.info(f"Executing function '{function_name}' from {target_module_id}...")

        # Execute the function, passing context_dict and supabase client
        # The module function is expected to return a dict of updates
        context_updates = run_function(context_dict, supabase_client)

        if isinstance(context_updates, dict):
            context_dict.update(context_updates)
            logger.info(f"Updated context_dict with: {context_updates}")
        else:
            logger.warning(f"Module {target_module_id} did not return a dictionary. Context not updated.")

        logger.info(f"Module {target_module_id} executed successfully.")
        # Log success to Pipeline_Log
        log_to_supabase(supabase_client, 'Pipeline_Log', {
            'module_id': target_module_id,
            'module_version': module_version,
            'message': 'Module executed successfully.',
            'stage': 'module_execution',
            'log_level': 'INFO',
            'context_snapshot': context_dict # Log final context after module run
        })

    except ImportError as e:
        logger.error(f"Failed to import module {module_import_path}: {e}", exc_info=True)
        log_to_supabase(supabase_client, 'Error_Log', {
            'module_id': target_module_id,
            'error_message': f"ImportError: {e}",
            'traceback': str(e),
            'stage': 'module_import'
        })
        sys.exit(1)
    except AttributeError as e:
        logger.error(f"Attribute error in module {target_module_id}: {e}", exc_info=True)
        log_to_supabase(supabase_client, 'Error_Log', {
            'module_id': target_module_id,
            'error_message': f"AttributeError: {e}",
            'traceback': str(e),
            'stage': 'module_execution'
        })
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error executing module {target_module_id}: {e}", exc_info=True)
        # Log error to Error_Log table in Supabase
        log_to_supabase(supabase_client, 'Error_Log', {
            'module_id': target_module_id,
            'module_version': module_version if 'module_version' in locals() else 'unknown',
            'error_message': f"Runtime Error: {e}",
            'traceback': logging.Formatter().formatException(sys.exc_info()),
            'stage': 'module_execution',
            'context_snapshot': context_dict
        })
        sys.exit(1)

    # --- End of Phase 0/1 Basic Setup ---

    logger.info("Pipeline orchestrator finished successfully.")

if __name__ == "__main__":
    main() 