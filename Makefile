ifeq ($(OS),Windows_NT)
SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command
endif

.PHONY: help hello update install lint test coverage run

help:
	@echo Targets are help, hello, update and check
update:
	uv lock
	uv sync
hello:
	uv run hello.py
lint:
	uv run ruff check
test:
	uv run pytest --cov-report=html --cov=src
	open htmlcov/index.html
coverage:
	open htmlcov/index.html
install:
	uv add --dev ruff
	uv add --dev pytest
	uv add --dev pytest-coverage
run:
	uv run flask --app tasktrail --debug run --port 8000