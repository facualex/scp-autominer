#!/bin/bash

current_dir=$(dirname "$0")  # Get the directory of the script

# Start the virtual environment (assuming you're using a virtual environment)
source "$current_dir/autominer-venv/bin/activate"

# Run the Python script with the virtual environment
"$current_dir/autominer-venv/bin/python" "$current_dir/main.py"

# Use 'read' to mimic 'pause' and wait for a key press
read -p "Press Enter to exit..."