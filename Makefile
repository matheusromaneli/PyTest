PYTHON := .venv/bin/python

install:
	uv venv
	uv pip install -e .[dev]

qa:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m mypy .
	$(PYTHON) -m pytest .
