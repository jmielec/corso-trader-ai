#!/bin/bash

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Print success message
echo "Python environment setup complete" 