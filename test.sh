#!/bin/sh

# Ensure virtual environment is set up
uv venv --clear
uv pip install -e ".[dev]"

# Run tests
uv run pytest -vv
