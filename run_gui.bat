@echo off

if not exist ".venv" (
    echo Creating virtual environment...
    uv venv
)

echo Installing dependencies...
uv pip install -e ".[dev]"

echo Starting GUI...
uv run python main.py -gui
