install-uv:
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv

setup: install-uv
	uv python install 3.13
	uv sync --all-extras
	uv pip install -e . 
	@echo "Python environment setup complete"

# Run all tests
test:
	uv run pytest tests -vv

# Run formatting and type checking
lint:
	uv run ruff check . --fix
	uv run mypy .

# Clean cache files
clean:
	rm -rf .venv/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache