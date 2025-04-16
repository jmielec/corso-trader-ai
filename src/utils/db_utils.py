import os
import logging
from supabase import create_client, Client

logger = logging.getLogger(__name__)

def get_supabase_client() -> Client | None:
    """Initializes and returns a Supabase client instance.

    Uses SUPABASE_URL and SUPABASE_SERVICE_KEY environment variables.
    Returns None if connection fails or variables are missing.
    """
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY") # Use the service role key

    if not supabase_url or not supabase_key:
        logger.error("SUPABASE_URL or SUPABASE_SERVICE_KEY environment variables not set.")
        return None

    try:
        # Ensure key is not logged directly if it's sensitive
        logger.info(f"Attempting to connect to Supabase URL: {supabase_url}")
        supabase: Client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client created successfully.")
        # Optional: Add a simple query to test the connection?
        # For example: supabase.table('some_table').select('id', count='exact').limit(1).execute()
        return supabase
    except Exception as e:
        logger.error(f"Failed to create Supabase client: {e}", exc_info=True)
        return None

# --- Placeholder for Module Registry Query --- #

def query_module_registry(client: Client, module_id: str) -> dict | None:
    """Queries the Module_Registry table for a specific active module.

    Args:
        client: The Supabase client instance.
        module_id: The ID of the module to query.

    Returns:
        A dictionary containing the module details if found and active,
        otherwise None.
    """
    if not client:
        logger.error("Supabase client is not available for query_module_registry.")
        return None

    try:
        logger.info(f"Querying Module_Registry for active module_id: {module_id}")
        response = (
            client.table('Module_Registry')
            .select("*")
            .eq('module_id', module_id)
            .eq('is_active', True)
            .limit(1)
            .execute()
        )
        logger.debug(f"Supabase response data: {response.data}")

        if response.data:
            logger.info(f"Found active module details for {module_id}.")
            return response.data[0]
        else:
            logger.warning(f"Module '{module_id}' not found or is not active in the registry.")
            return None

    except Exception as e:
        logger.error(f"Error querying Module_Registry for {module_id}: {e}", exc_info=True)
        return None

# --- Placeholder for Logging to DB --- #

def log_to_supabase(client: Client, log_table: str, log_data: dict):
    """Logs data to a specified Supabase table (e.g., Pipeline_Log, Error_Log)."""
    if not client:
        logger.error(f"Supabase client is not available for logging to {log_table}.")
        return

    try:
        response = client.table(log_table).insert(log_data).execute()
        # Minimal logging here to avoid log loops
        if len(response.data) == 0:
             print(f"Warning: Failed to insert log into {log_table}. Data: {log_data}. Response: {response}")

    except Exception as e:
        # Avoid logging errors about logging to prevent infinite loops
        # Print directly or handle carefully
        print(f"CRITICAL: Failed to log to Supabase table {log_table}: {e}. Data: {log_data}") 