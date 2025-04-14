import json
import sys
from typing import Dict, Any, Optional # Import standard types

# Configure basic logging (can be enhanced later)
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sample_processor(symbol: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    A sample processing function demonstrating the basic structure.

    Args:
        symbol (str): The instrument symbol to process (e.g., 'BTC/USDT').
        context (Optional[Dict[str, Any]]): An optional dictionary containing
                                             input context data passed from n8n
                                             or previous steps. Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary containing the results or output context.
                        Must be JSON serializable if passing back to n8n via stdout.
    """
    logging.info(f"Processing symbol: {symbol}")

    if context:
        logging.info(f"Received context: {context}")
    else:
        logging.info("No input context received.")
        context = {} # Initialize if none provided

    # --- Start of Module-Specific Logic ---

    # Example: Add a processed flag to the context
    processed_status = f"{symbol}_processed_ok"
    output_data = {
        "status": processed_status,
        "input_symbol": symbol
        # Add more results here as needed
    }

    # Example: Maybe merge results back into the input context if desired
    updated_context = context.copy() # Avoid modifying the original input dict directly
    updated_context.update(output_data)

    # --- End of Module-Specific Logic ---

    logging.info(f"Finished processing for {symbol}. Output: {output_data}")

    # Return the results (ensure it's JSON serializable for n8n stdout)
    return output_data # Or return updated_context if you want everything passed on


if __name__ == "__main__":
    """
    This block allows the script to be run directly from the command line
    for testing. It simulates getting arguments like n8n might provide.
    """
    logging.info("Running example_module.py directly...")

    # Example: Simulate command-line arguments (e.g., symbol)
    # In a real scenario, n8n might pass arguments or JSON via stdin
    test_symbol = "BTC/USDT"
    if len(sys.argv) > 1:
         test_symbol = sys.argv[1] # Allow overriding symbol via command line argument

    # Example: Simulate passing context as a JSON string (like n8n might)
    test_context_json = None
    # To test context passing:
    # test_context_json = '{"previous_step": "data_loaded", "some_value": 123}'

    input_context = None
    if test_context_json:
         try:
             input_context = json.loads(test_context_json)
         except json.JSONDecodeError:
             logging.error("Failed to decode test context JSON.")


    # Call the main processing function
    result = sample_processor(test_symbol, input_context)

    # Print the result as JSON to stdout (simulating output for n8n)
    print(json.dumps(result, indent=2))

    logging.info("Direct execution finished.")

