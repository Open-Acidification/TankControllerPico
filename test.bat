@echo off

if not exist ".venv" (
    echo Creating virtual environment...
    uv venv --clear
)

echo Installing dependencies...
uv pip install -e ".[dev]"

echo Running tests...
uv run pytest -vv