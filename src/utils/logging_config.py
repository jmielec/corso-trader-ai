import logging
import sys

# TODO: Implement more sophisticated logging configuration
# - File handler
# - Supabase handler (logging to DB table)
# - Standardized JSON format
# - Injecting module_id, version, run_id automatically

def setup_logging(log_level=logging.INFO):
    """Basic console logging setup."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout, # Ensure logs go to stdout for Render to capture
    )
    # You might want to silence overly verbose libraries here if needed
    # logging.getLogger("some_library").setLevel(logging.WARNING)

    return logging.getLogger()

# Example usage (in other modules):
# from src.utils.logging_config import setup_logging
# logger = setup_logging()
# logger.info("This is an info message.") 