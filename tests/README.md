# Test Automation Framework

This directory contains the test automation framework for the g4j project.

## Overview

The test automation framework is built using pytest and provides a comprehensive suite of test utilities, fixtures, and sample tests.

## Structure

```
tests/
├── __init__.py              # Package initialization
├── conftest.py              # Pytest configuration and shared fixtures
├── test_sample.py           # Sample test cases demonstrating features
├── test_helpers_demo.py     # Tests demonstrating helper utilities
├── utils/                   # Test utilities package
│   ├── __init__.py
│   └── test_helpers.py      # Helper functions and utilities
└── README.md                # This file
```

## Installation

Install test dependencies:

```bash
pip install -r requirements-test.txt
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_sample.py
```

### Run specific test class
```bash
pytest tests/test_sample.py::TestBasicFunctionality
```

### Run specific test method
```bash
pytest tests/test_sample.py::TestBasicFunctionality::test_simple_assertion
```

### Run tests with specific markers
```bash
# Run only smoke tests
pytest -m smoke

# Run only integration tests
pytest -m integration

# Run all except slow tests
pytest -m "not slow"
```

### Run tests with coverage
```bash
pytest --cov=. --cov-report=html
```

### Run tests in parallel
```bash
pytest -n auto
```

### Run tests with detailed output
```bash
pytest -v -s
```

## Test Categories

The framework includes several test categories marked with pytest markers:

- **smoke**: Quick smoke tests for critical functionality
- **integration**: Integration tests between components
- **unit**: Unit tests for individual functions
- **slow**: Tests that take longer to execute
- **api**: API-related tests
- **ui**: UI-related tests

## Fixtures

### Available Fixtures

- **test_config**: Provides test configuration for the session
- **setup_teardown**: Setup and teardown for test functions
- **mock_data**: Provides mock data for testing

### Using Fixtures

```python
def test_example(test_config, mock_data):
    assert test_config["project_name"] == "g4j"
    assert "user" in mock_data
```

## Test Utilities

### Retry Decorator

Automatically retry flaky tests:

```python
from tests.utils.test_helpers import retry_on_failure

@retry_on_failure(max_attempts=3, delay=1.0)
def test_flaky_operation():
    # Test code here
    pass
```

### Wait Until

Wait for a condition to be met:

```python
from tests.utils.test_helpers import wait_until

def test_async_operation():
    wait_until(
        lambda: check_condition(),
        timeout=10.0,
        poll_interval=0.5
    )
```

### Test Data Generator

Generate mock test data:

```python
from tests.utils.test_helpers import TestDataGenerator

def test_with_generated_data():
    users = TestDataGenerator.generate_user_data(count=5)
    items = TestDataGenerator.generate_item_data(count=10)
```

### Assertion Helper

Common assertion utilities:

```python
from tests.utils.test_helpers import AssertionHelper

def test_validations():
    assert AssertionHelper.assert_valid_email("test@example.com")
    assert AssertionHelper.assert_in_range(5, 1, 10)
    assert AssertionHelper.assert_dict_contains_keys(data, ["id", "name"])
```

## Best Practices

1. **Test Naming**: Use descriptive test names that explain what is being tested
2. **Test Organization**: Group related tests in classes
3. **Fixtures**: Use fixtures for common setup/teardown and data
4. **Markers**: Tag tests with appropriate markers for easy filtering
5. **Assertions**: Use clear assertion messages
6. **Parametrization**: Use pytest.mark.parametrize for testing multiple scenarios
7. **Isolation**: Ensure tests are independent and can run in any order
8. **Clean Up**: Always clean up resources in teardown

## Continuous Integration

The test suite is designed to run in CI/CD pipelines. Example CI command:

```bash
pytest -v --tb=short --junitxml=test-results.xml --cov=. --cov-report=xml
```

## Contributing

When adding new tests:

1. Follow the existing test structure and naming conventions
2. Add appropriate markers to categorize tests
3. Use existing fixtures and utilities where applicable
4. Document complex test scenarios
5. Ensure tests are independent and repeatable

## Support

For issues or questions about the test framework, please refer to the project documentation or contact the development team.
