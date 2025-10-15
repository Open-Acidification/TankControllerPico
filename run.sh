#!/bin/sh

# Ensure virtual environment is set up
uv venv --clear
uv pip install -e ".[dev]"

# Run the GUI application
uv run python main.py
