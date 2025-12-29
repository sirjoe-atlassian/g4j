.PHONY: help install test test-unit test-integration test-e2e test-smoke test-regression clean lint format

help:
	@echo "Available commands:"
	@echo "  make install           - Install dependencies"
	@echo "  make test              - Run all tests"
	@echo "  make test-unit         - Run unit tests only"
	@echo "  make test-integration  - Run integration tests only"
	@echo "  make test-e2e          - Run end-to-end tests only"
	@echo "  make test-smoke        - Run smoke tests only"
	@echo "  make test-regression   - Run regression tests"
	@echo "  make clean             - Clean generated files"
	@echo "  make lint              - Run linting"
	@echo "  make format            - Format code"

install:
	pip install -r requirements.txt

test:
	pytest

test-unit:
	pytest -m unit

test-integration:
	pytest -m integration

test-e2e:
	pytest -m e2e

test-smoke:
	pytest -m smoke

test-regression:
	pytest -m regression

test-parallel:
	pytest -n auto

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov reports
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete

lint:
	@echo "Install flake8 to run linting: pip install flake8"
	@echo "Then run: flake8 tests utils"

format:
	@echo "Install black to format code: pip install black"
	@echo "Then run: black tests utils"
