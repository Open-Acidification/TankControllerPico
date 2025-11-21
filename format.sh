#!/bin/bash

# Ensure virtual environment is set up
uv venv --clear
uv pip install -e ".[dev]"

# Spell check
uv run codespell -f -w .

# Format Python
uv run black .
uv run isort .
uv run flake8 .
uv run pylint main.py src/ tests/

# Clean up
find . -name ".pytest_cache" -type d -exec /bin/rm -rf {} +
find . -name "__pycache__" -type d -exec /bin/rm -rf {} +
