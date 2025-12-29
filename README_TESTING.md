# Test Automation Framework

## Overview

This test automation framework provides a comprehensive solution for automated testing with built-in reporting, data validation, and test utilities.

## Features

- **Base Test Classes**: Reusable base classes with setup/teardown hooks
- **Test Reporting**: Automatic generation of JSON test reports
- **Data Validation**: Helper classes for validating different data types
- **API Testing**: Utilities for API response validation
- **Test Data Generation**: Generate test data on-the-fly
- **Logging**: Comprehensive logging for debugging
- **Configuration**: JSON-based configuration management

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── test_automation_framework.py   # Main framework code
├── test_config.json               # Test configuration
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── tests/                         # Test directory (create as needed)
└── test_reports/                  # Generated reports (auto-created)
```

## Usage

### Running Tests

#### Using the built-in framework:
```bash
python test_automation_framework.py
```

#### Using pytest:
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_example.py

# Run tests with specific marker
pytest -m smoke

# Run with coverage
pytest --cov=. --cov-report=html
```

### Writing Tests

#### Basic Test Example:
```python
from test_automation_framework import BaseTestCase, DataValidator

class MyTestSuite(BaseTestCase):
    
    def test_example(self):
        """Example test case"""
        result = some_function()
        self.assertEqual(result, expected_value)
        DataValidator.validate_not_empty(result, "Result")
```

#### API Test Example:
```python
from test_automation_framework import BaseTestCase, APITestHelper
import requests

class APITestSuite(BaseTestCase):
    
    def test_api_endpoint(self):
        """Test API endpoint"""
        response = requests.get("http://api.example.com/users")
        APITestHelper.validate_response_status(response, 200)
        APITestHelper.validate_json_schema(
            response.json(), 
            ['id', 'name', 'email']
        )
```

### Test Data Generation

```python
from test_automation_framework import TestDataGenerator

# Generate single test user
user = TestDataGenerator.generate_test_user(1)

# Generate multiple test users
users = TestDataGenerator.generate_test_data_set(10, 'user')
```

### Data Validation

```python
from test_automation_framework import DataValidator

# Validate not empty
DataValidator.validate_not_empty(value, "Field Name")

# Validate type
DataValidator.validate_type(value, int, "User ID")

# Validate numeric range
DataValidator.validate_range(value, 0, 100, "Score")

# Validate regex pattern
DataValidator.validate_regex(email, r'^[\w\.-]+@[\w\.-]+\.\w+$', "Email")
```

## Configuration

Edit `test_config.json` to customize:
- Test environment settings
- API base URLs and timeouts
- Reporting options
- Logging configuration
- Parallel execution settings

## Test Reports

After test execution, reports are generated in JSON format:
- `test_report.json`: Detailed test results with pass/fail status, duration, and errors

## Pytest Markers

Available test markers:
- `@pytest.mark.smoke`: Quick smoke tests
- `@pytest.mark.regression`: Regression test suite
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.api`: API tests
- `@pytest.mark.slow`: Tests that take longer to run

Example usage:
```python
import pytest

@pytest.mark.smoke
def test_critical_feature():
    """Critical smoke test"""
    assert True
```

## Best Practices

1. **Organize Tests**: Group related tests in classes
2. **Use Descriptive Names**: Test names should describe what they test
3. **Keep Tests Independent**: Each test should run independently
4. **Use Fixtures**: Leverage pytest fixtures for test data setup
5. **Add Documentation**: Include docstrings for test classes and methods
6. **Validate Thoroughly**: Use validation helpers for comprehensive checks
7. **Log Appropriately**: Use logging for debugging, not print statements

## Extending the Framework

### Adding Custom Validators

```python
class CustomValidator:
    @staticmethod
    def validate_custom_logic(value, expected):
        assert custom_check(value, expected), "Custom validation failed"
```

### Adding Custom Test Helpers

```python
class DatabaseTestHelper:
    @staticmethod
    def validate_db_connection(connection):
        assert connection.is_connected(), "Database connection failed"
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`
2. **Test Discovery**: Make sure test files start with `test_` or end with `_test.py`
3. **Configuration Issues**: Verify `test_config.json` is properly formatted

## License

See `licence.md` for license information.

## Support

For issues and questions, refer to the project documentation or contact the development team.
