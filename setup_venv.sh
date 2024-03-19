#!/bin/bash

# Check for requirements.txt file
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found in the current directory."
    exit 1
fi

# Create a virtual environment named 'venv' in the current directory
python3 -m venv venv

# Activate the virtual environment
# Note: This syntax is for bash. If you're using a different shell, the activation command might differ.
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Virtual environment created and dependencies installed."