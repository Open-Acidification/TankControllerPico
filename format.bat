@echo off 

if not exist ".venv" (
    echo Creating virtual environment...
    uv venv
)

echo Installing dependencies...
uv pip install -e ".[dev]"

echo spell checking...
uv run codespell -f -w .

echo Formatting Python...
uv run black .
uv run isort .
uv run flake8 .
uv run pylint main.py src/ tests/
uv run ruff check --fix .
uv run ruff format .

echo Cleaning up...
for /d /r %%d in (.pytest_cache) do @if exist "%%d" rmdir /s /q "%%d"
for /d /r %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
