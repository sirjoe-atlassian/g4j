# Test Automation Framework

**Jira Issue:** [DEV-4 - Test automation generate code](https://jyang4-test.atlassian.net/browse/DEV-4)

## Overview

This test automation framework provides a comprehensive solution for API, UI, and integration testing. It uses Python with pytest as the core testing framework.

## Project Structure

```
.
├── licence.md                          # MIT License
├── README.md                           # Project README
├── README_TEST_AUTOMATION.md           # This file
├── test_automation_framework.py        # Main framework with unittest examples
├── conftest.py                         # Pytest configuration and fixtures
├── pytest.ini                          # Pytest settings
├── requirements.txt                    # Python dependencies
└── tests/                              # Test directory
    ├── __init__.py
    ├── test_api_examples.py            # API test examples
    ├── test_ui_examples.py             # UI test examples
    └── test_integration.py             # Integration test examples
```

## Features

### 1. Test Framework Components

- **TestBase**: Base class for unittest-based tests with setup/teardown methods
- **TestDataGenerator**: Utility for generating test data
- **TestHelper**: Helper methods for common assertions
- **Custom Fixtures**: Reusable pytest fixtures for test configuration

### 2. Test Categories

- **API Tests**: RESTful API testing with mock client
- **UI Tests**: Web UI testing with browser automation
- **Integration Tests**: End-to-end workflow testing
- **Smoke Tests**: Quick validation tests
- **Regression Tests**: Comprehensive test coverage

### 3. Test Markers

Tests are organized using pytest markers:
- `@pytest.mark.api` - API tests
- `@pytest.mark.ui` - UI tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.smoke` - Smoke tests
- `@pytest.mark.regression` - Regression tests
- `@pytest.mark.slow` - Long-running tests

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Verify installation:
```bash
pytest --version
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test Categories

```bash
# Run only API tests
pytest -m api

# Run only UI tests
pytest -m ui

# Run smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression
```

### Run Specific Test Files

```bash
# Run API tests only
pytest tests/test_api_examples.py

# Run UI tests only
pytest tests/test_ui_examples.py

# Run integration tests only
pytest tests/test_integration.py
```

### Run with Different Verbosity

```bash
# Verbose output
pytest -v

# Very verbose output
pytest -vv

# Quiet mode
pytest -q
```

### Run Tests in Parallel

```bash
# Run tests using 4 workers
pytest -n 4
```

### Generate Test Reports

```bash
# Generate HTML report
pytest --html=test-report.html --self-contained-html

# Generate coverage report
pytest --cov=. --cov-report=html
```

## Using the Framework

### Example 1: Running Unittest-based Tests

```bash
python test_automation_framework.py
```

### Example 2: Writing New API Tests

```python
import pytest

@pytest.mark.api
class TestNewAPI:
    def test_endpoint(self, api_client):
        response = api_client.get('/new-endpoint')
        assert response['status'] == 200
```

### Example 3: Writing New UI Tests

```python
import pytest

@pytest.mark.ui
class TestNewPage:
    def test_page_loads(self, browser_driver, test_config):
        browser_driver.get(f"{test_config['base_url']}/new-page")
        assert browser_driver.current_url.endswith('/new-page')
```

### Example 4: Using Test Fixtures

```python
def test_with_sample_data(sample_user_data):
    """Test using the sample_user_data fixture"""
    assert sample_user_data['username'] == 'testuser'
    assert sample_user_data['email'] == 'testuser@example.com'
```

## Test Data Generation

The framework includes a `TestDataGenerator` class for creating test data:

```python
from test_automation_framework import TestDataGenerator

# Generate user data
users = TestDataGenerator.generate_user_data(count=5)

# Generate product data
products = TestDataGenerator.generate_product_data(count=10)
```

## Configuration

### pytest.ini

Configure test execution settings in `pytest.ini`:
- Test discovery patterns
- Logging configuration
- Coverage settings
- HTML report generation

### conftest.py

Define fixtures and hooks in `conftest.py`:
- `test_config`: Test configuration fixture
- `sample_user_data`: Sample user data fixture
- `api_client`: Mock API client fixture
- `browser_driver`: Mock browser driver fixture

## Best Practices

1. **Use Descriptive Test Names**: Test method names should clearly describe what is being tested
2. **Follow AAA Pattern**: Arrange, Act, Assert in each test
3. **Use Fixtures**: Leverage pytest fixtures for setup and teardown
4. **Add Markers**: Tag tests with appropriate markers for easy filtering
5. **Log Important Events**: Use logging to track test execution
6. **Parametrize Tests**: Use `@pytest.mark.parametrize` for data-driven tests
7. **Keep Tests Independent**: Each test should be able to run independently

## Extending the Framework

### Adding New Fixtures

Add new fixtures to `conftest.py`:

```python
@pytest.fixture
def new_fixture():
    # Setup code
    yield fixture_value
    # Teardown code
```

### Adding New Test Helpers

Extend the `TestHelper` class in `test_automation_framework.py`:

```python
class TestHelper:
    @staticmethod
    def new_helper_method():
        # Helper logic
        pass
```

### Adding Real API/UI Integration

Replace mock implementations with real API clients and Selenium WebDriver:

```python
# For API testing
import requests

# For UI testing
from selenium import webdriver
from selenium.webdriver.common.by import By
```

## CI/CD Integration

### Example GitHub Actions Workflow

```yaml
name: Test Automation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest --html=test-report.html
      - name: Upload test report
        uses: actions/upload-artifact@v2
        with:
          name: test-report
          path: test-report.html
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed: `pip install -r requirements.txt`
2. **Test Discovery Issues**: Check `pytest.ini` for correct test patterns
3. **Fixture Errors**: Verify fixtures are defined in `conftest.py`
4. **Marker Warnings**: Register all markers in `pytest.ini`

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

1. Write tests following the existing patterns
2. Add appropriate markers to new tests
3. Update documentation for new features
4. Ensure all tests pass before submitting changes

## Support

For issues related to this test automation framework, please refer to:
- Jira Issue: [DEV-4](https://jyang4-test.atlassian.net/browse/DEV-4)
- Parent Task: [DEV-2](https://jyang4-test.atlassian.net/browse/DEV-2)

## Next Steps

1. Replace mock implementations with real API clients and Selenium WebDriver
2. Configure test environment variables in `.env` file
3. Set up CI/CD pipeline for automated test execution
4. Implement page object model for UI tests
5. Add more comprehensive test data generators
6. Integrate with test reporting tools (e.g., Allure)
