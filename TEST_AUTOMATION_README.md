# Test Automation Framework for g4j

This document provides comprehensive documentation for the test automation framework implemented for the g4j project.

## Overview

The test automation framework provides a robust, scalable solution for testing with support for:
- **Unit Testing**: Test individual components and functions
- **Integration Testing**: Test interactions between components
- **Pytest Framework**: Modern, feature-rich testing with pytest
- **Custom Framework**: Standalone test framework with detailed reporting
- **Flexible Configuration**: Environment-based configuration management
- **Multiple Report Formats**: JSON, HTML, and console reporting

## Project Structure

```
g4j/
├── licence.md                      # MIT License
├── README.md                        # Project README
├── TEST_AUTOMATION_README.md        # This file
├── test_automation_framework.py     # Custom test framework
├── pytest_tests.py                  # Pytest-based tests
├── test_config.py                   # Test configuration and utilities
├── requirements-test.txt            # Test dependencies
├── pytest.ini                       # Pytest configuration
└── run_tests.sh                     # Test execution script
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Install test dependencies:
```bash
pip install -r requirements-test.txt
```

Or use the test script with auto-install:
```bash
./run_tests.sh --install-deps
```

## Running Tests

### Quick Start

Run all tests with the default configuration:
```bash
./run_tests.sh
```

### Test Execution Options

#### Run All Tests
```bash
./run_tests.sh all
```

#### Run Unit Tests Only
```bash
./run_tests.sh unit
```

#### Run Integration Tests Only
```bash
./run_tests.sh integration
```

#### Run Smoke Tests
```bash
./run_tests.sh smoke
```

#### Run with Coverage Report
```bash
./run_tests.sh coverage
```

#### Run Custom Framework
```bash
./run_tests.sh framework
```

#### Run Quick Tests (Exclude Slow Tests)
```bash
./run_tests.sh quick
```

### Direct Execution

#### Using Pytest
```bash
# Run all tests
pytest pytest_tests.py -v

# Run specific test class
pytest pytest_tests.py::TestBasicOperations -v

# Run specific test method
pytest pytest_tests.py::TestBasicOperations::test_addition -v

# Run tests by marker
pytest pytest_tests.py -m smoke -v
pytest pytest_tests.py -m "not slow" -v

# Run with coverage
pytest pytest_tests.py --cov=. --cov-report=html
```

#### Using Custom Framework
```bash
python3 test_automation_framework.py
```

## Test Framework Components

### 1. Custom Test Framework (`test_automation_framework.py`)

A standalone test automation framework with the following features:

**Key Classes:**
- `TestResult`: Data class for storing test execution results
- `TestReporter`: Generates reports in JSON and console formats
- `BaseTestCase`: Abstract base class for all test cases
- `UnitTestCase`: Implementation for unit tests
- `IntegrationTestCase`: Implementation for integration tests
- `TestSuite`: Organizes and executes multiple test cases
- `TestRunner`: Main coordinator for test execution

**Usage Example:**
```python
from test_automation_framework import TestSuite, UnitTestCase, TestRunner

# Create a test suite
suite = TestSuite("My Tests")

# Define test function
def test_example():
    assert 1 + 1 == 2

# Add test to suite
suite.add_test(UnitTestCase("Test Example", test_example))

# Run tests
runner = TestRunner()
runner.add_suite(suite)
runner.run_all_suites()
```

### 2. Pytest Framework (`pytest_tests.py`)

Modern testing framework with pytest featuring:

**Test Classes:**
- `TestBasicOperations`: Basic mathematical and string operations
- `TestDataStructures`: List, dictionary, and set operations
- `TestWithFixtures`: Tests using pytest fixtures
- `TestParametrized`: Parametrized test cases
- `TestExceptions`: Exception handling tests
- `TestSmokeSuite`: Critical smoke tests
- `TestIntegration`: Integration test scenarios
- `TestSlowOperations`: Long-running tests
- `TestConditional`: Conditional test execution

**Fixtures:**
- `sample_data`: Provides sample user data
- `config`: Provides test configuration

**Test Markers:**
- `@pytest.mark.smoke`: Critical functionality tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.slow`: Long-running tests
- `@pytest.mark.skip`: Skip test execution
- `@pytest.mark.xfail`: Expected failures

### 3. Test Configuration (`test_config.py`)

Configuration management and utilities:

**TestConfig Class:**
```python
from test_config import TestConfig

# Load from environment variables
config = TestConfig.from_env()

# Access configuration
print(config.base_url)
print(config.timeout)
```

**TestDataGenerator:**
```python
from test_config import TestDataGenerator

# Generate test users
users = TestDataGenerator.generate_user_data(count=5)

# Generate API response
response = TestDataGenerator.generate_api_response(
    status="success",
    data={"message": "Test data"}
)
```

**TestAssertion Utilities:**
```python
from test_config import TestAssertion

# Custom assertions
TestAssertion.assert_dict_contains(actual_dict, expected_dict)
TestAssertion.assert_list_length(my_list, 5)
TestAssertion.assert_response_status(response, "success")
```

**TestHelper Utilities:**
```python
from test_config import TestHelper

# Wait for condition
TestHelper.wait_for_condition(lambda: condition_is_true(), timeout=10)

# Setup test directory
TestHelper.setup_test_directory("./test_output")

# Cleanup test files
TestHelper.cleanup_test_files("./temp", pattern="*test*")
```

## Configuration

### Environment Variables

Configure tests using environment variables:

```bash
export TEST_ENV=development
export BASE_URL=http://localhost:8000
export TEST_TIMEOUT=30
export RETRY_COUNT=3
export REPORT_PATH=./test_reports
export LOG_LEVEL=INFO
```

### Pytest Configuration (`pytest.ini`)

Customize pytest behavior:
- Test discovery patterns
- Command-line options
- Test markers
- Coverage settings

## Test Reports

### JSON Report
After test execution, reports are generated:
- `final_test_report.json`: Complete test results
- `test_report.json`: Individual suite results

**Report Structure:**
```json
{
  "total_tests": 10,
  "passed": 8,
  "failed": 2,
  "skipped": 0,
  "total_execution_time": 1.234,
  "tests": [
    {
      "test_name": "Test Example",
      "status": "PASS",
      "execution_time": 0.123,
      "error_message": null,
      "timestamp": "2025-01-01T00:00:00"
    }
  ]
}
```

### HTML Coverage Report
Generate with pytest:
```bash
pytest --cov=. --cov-report=html
```
View at: `htmlcov/index.html`

### Console Report
Automatically displayed after test execution with:
- Total test count
- Pass/fail/skip counts
- Success rate
- Failed test details

## Best Practices

### Writing Tests

1. **Use Descriptive Names**
```python
def test_user_registration_with_valid_email():
    # Test implementation
```

2. **Follow AAA Pattern** (Arrange, Act, Assert)
```python
def test_addition():
    # Arrange
    a = 2
    b = 3
    
    # Act
    result = a + b
    
    # Assert
    assert result == 5
```

3. **Use Fixtures for Setup**
```python
@pytest.fixture
def database_connection():
    conn = create_connection()
    yield conn
    conn.close()

def test_database_query(database_connection):
    result = database_connection.query("SELECT 1")
    assert result is not None
```

4. **Parametrize Similar Tests**
```python
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_square(input, expected):
    assert input ** 2 == expected
```

5. **Use Appropriate Markers**
```python
@pytest.mark.smoke
def test_critical_feature():
    assert critical_function() == expected_result

@pytest.mark.slow
def test_performance():
    # Long-running test
```

### Test Organization

- Group related tests in classes
- Use separate files for different test types
- Keep tests independent and isolated
- Clean up test data after execution

## Extending the Framework

### Adding New Test Types

```python
from test_automation_framework import BaseTestCase, TestResult

class CustomTestCase(BaseTestCase):
    def run(self) -> TestResult:
        # Implement custom test logic
        pass
```

### Creating Custom Fixtures

```python
@pytest.fixture(scope="session")
def global_resource():
    # Setup
    resource = create_resource()
    yield resource
    # Teardown
    cleanup_resource(resource)
```

### Adding Custom Assertions

```python
class TestAssertion:
    @staticmethod
    def assert_custom_condition(value):
        assert condition(value), f"Custom assertion failed for {value}"
```

## Troubleshooting

### Common Issues

**Issue: Tests not discovered**
- Ensure test files match pattern: `test_*.py` or `*_test.py`
- Check test functions start with `test_`
- Verify pytest.ini configuration

**Issue: Import errors**
- Install dependencies: `pip install -r requirements-test.txt`
- Check Python path configuration

**Issue: Slow test execution**
- Run quick tests: `./run_tests.sh quick`
- Use parallel execution: `pytest -n auto`
- Review and optimize slow tests

## Continuous Integration

### GitHub Actions Example

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r requirements-test.txt
    - name: Run tests
      run: ./run_tests.sh coverage
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

## Support and Contribution

For issues, questions, or contributions, please refer to the project's issue tracker.

## License

This test automation framework is part of the g4j project and is licensed under the MIT License. See `licence.md` for details.
