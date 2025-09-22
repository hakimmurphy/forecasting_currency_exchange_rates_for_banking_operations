import json
import sys

# Replace with your notebook path if running outside the notebook directory
notebook_path = "forecasting_currency_exchange_rates_for_banking_operations.ipynb"

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Check if metadata exists
if 'metadata' not in notebook:
    notebook['metadata'] = {}

# Check if widgets exists in metadata
if 'widgets' in notebook['metadata']:
    # Add state if it doesn't exist
    if 'state' not in notebook['metadata']['widgets']:
        notebook['metadata']['widgets']['state'] = {}
        print("Added missing 'state' key to widgets metadata")
else:
    # If no widgets metadata at all, add an empty one with state
    notebook['metadata']['widgets'] = {"state": {}}
    print("Added widgets metadata with state")

# Save the modified notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Notebook {notebook_path} has been updated")