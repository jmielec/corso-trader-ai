import logging
from typing import Dict, Any

# Use the shared logger setup
# Note: This assumes the orchestrator sets up logging beforehand.
logger = logging.getLogger(__name__)

# Function signature must match what the orchestrator expects to call.
# We'll pass the context_dict and potentially the supabase client.

def run(context_dict: Dict[str, Any], supabase_client: Any | None = None) -> Dict[str, Any]:
    """A simple example module function.

    Args:
        context_dict: The dictionary holding pipeline context.
        supabase_client: The initialized Supabase client (optional for this module).

    Returns:
        A dictionary containing updates to the context_dict.
    """
    module_id = "hello_module_v1" # Hardcoded for logging
    logger.info(f"[{module_id}] Executing hello_module_v1...")

    # 1. Read from context (if needed)
    # previous_data = context_dict.get("some_key", "default_value")

    # 2. Perform module logic
    message = "Hello from the first registered module!"
    logger.info(f"[{module_id}] Generated message: {message}")

    # 3. Update context dictionary
    context_updates = {
        "hello_message": message,
        "module_executed": module_id
    }

    logger.info(f"[{module_id}] Finished execution.")
    return context_updates

# Example of direct execution for testing (optional)
if __name__ == "__main__":
    # Basic setup for direct testing
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    test_context = {}
    print(f"Initial context: {test_context}")

    # Simulate running the module function
    updates = run(test_context)
    test_context.update(updates)

    print(f"Final context: {test_context}") 