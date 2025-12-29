# Test Automation for g4j

This directory contains automated test suites for the g4j project.

## Test Files

- `test_example.py` - Unit tests using Python's built-in unittest framework
- `test_pytest_example.py` - Tests using pytest framework with fixtures and parametrization
- `conftest.py` - Shared pytest fixtures and configuration

## Running Tests

### Using unittest

```bash
# Run all unittest tests
python -m unittest discover tests

# Run specific test file
python tests/test_example.py

# Run with verbose output
python -m unittest discover tests -v
```

### Using pytest

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_pytest_example.py

# Run tests matching a pattern
pytest -k "test_string"

# Run with coverage report
pytest --cov=. --cov-report=html

# Skip slow tests
pytest -m "not slow"
```

## Test Structure

### unittest Tests

The unittest tests follow the standard Python testing framework:
- Test classes inherit from `unittest.TestCase`
- Test methods start with `test_`
- Uses `setUp()` and `tearDown()` for test fixtures
- Supports class-level fixtures with `setUpClass()` and `tearDownClass()`

### pytest Tests

The pytest tests leverage pytest's powerful features:
- Simple assert statements (no special assertion methods needed)
- Fixtures defined in `conftest.py`
- Parametrized tests for data-driven testing
- Test marking for categorization and selective execution
- Better error messages and output

## Requirements

Install testing dependencies:

```bash
pip install pytest pytest-cov
```

## Best Practices

1. **Test Isolation**: Each test should be independent and not rely on other tests
2. **Clear Names**: Use descriptive test method names that explain what is being tested
3. **Arrange-Act-Assert**: Structure tests with clear setup, execution, and verification phases
4. **Use Fixtures**: Leverage fixtures for common test data and setup
5. **Parametrize**: Use parametrized tests to test multiple scenarios efficiently
6. **Test Coverage**: Aim for high test coverage but focus on meaningful tests

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install pytest pytest-cov
    pytest --cov=. --cov-report=xml
```

## Contributing

When adding new tests:
1. Follow the existing test structure and naming conventions
2. Add appropriate documentation/docstrings
3. Ensure tests are isolated and repeatable
4. Update this README if adding new test categories or requirements
