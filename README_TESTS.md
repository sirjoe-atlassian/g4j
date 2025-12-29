# Test Automation Framework

A flexible and extensible Python-based test automation framework with support for multiple test types and comprehensive reporting.

## Features

- **Flexible Test Structure**: Built on Python's unittest framework
- **Custom Assertions**: Extended assertion methods for common test scenarios
- **Detailed Reporting**: Generate reports in JSON and text formats
- **Test Results Tracking**: Comprehensive tracking of test execution results
- **Easy Extension**: Base test case class for creating custom test suites

## Installation

No additional dependencies required. The framework uses Python's standard library.

Requirements:
- Python 3.6 or higher

## Quick Start

### Running Example Tests

```bash
# Run the example test suite
python test_example.py

# Or run using the automation framework
python test_automation.py "test_example.py" "Example Test Suite"
```

### Creating Your Own Tests

1. Import the BaseTestCase class:

```python
from test_automation import BaseTestCase

class MyTestCase(BaseTestCase):
    def test_my_feature(self):
        result = my_function()
        self.assertEqual(result, expected_value)
```

2. Run your tests:

```bash
python test_automation.py "test_my*.py" "My Test Suite"
```

## Framework Components

### TestAutomationFramework

Main class for running test suites and generating reports.

**Key Methods:**
- `run_test_suite(test_loader, test_pattern)`: Execute tests matching the pattern
- `generate_report(output_format)`: Generate report in 'json' or 'text' format
- `save_report(filename, output_format)`: Save report to file

### BaseTestCase

Extended unittest.TestCase with additional functionality.

**Custom Assertions:**
- `assert_response_code(actual, expected, message)`: Assert HTTP response codes
- `assert_contains(container, item, message)`: Assert item exists in container

**Built-in Features:**
- Automatic test timing
- Setup and teardown logging

### TestResult

Stores individual test execution results.

**Attributes:**
- `test_name`: Name of the test
- `status`: PASSED, FAILED, or ERROR
- `duration`: Test execution time
- `error_message`: Error details (if any)
- `timestamp`: Test execution timestamp

## Usage Examples

### Example 1: Basic Test Execution

```python
#!/usr/bin/env python3
from test_automation import BaseTestCase

class CalculatorTest(BaseTestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)
```

### Example 2: API Testing

```python
from test_automation import BaseTestCase

class APITest(BaseTestCase):
    def test_api_endpoint(self):
        # Simulate API call
        response_code = 200
        response_data = {"status": "success"}
        
        self.assert_response_code(response_code, 200)
        self.assert_contains(response_data, "status")
```

### Example 3: Custom Test Suite

```python
from test_automation import TestAutomationFramework
import unittest

# Create framework instance
framework = TestAutomationFramework("My Custom Suite")

# Load tests
loader = unittest.TestLoader()
success = framework.run_test_suite(loader, "test_custom*.py")

# Generate reports
framework.save_report("results.json", "json")
framework.save_report("results.txt", "text")
```

## Report Formats

### JSON Report

```json
{
  "test_suite": "Example Test Suite",
  "start_time": "2025-01-01T10:00:00",
  "end_time": "2025-01-01T10:00:05",
  "total_tests": 10,
  "passed": 8,
  "failed": 1,
  "errors": 1,
  "results": [...]
}
```

### Text Report

```
================================================================================
Test Suite: Example Test Suite
================================================================================
Start Time: 2025-01-01 10:00:00
End Time: 2025-01-01 10:00:05
Total Tests: 10
Passed: 8
Failed: 1
Errors: 1
================================================================================
```

## Command Line Usage

```bash
# Run all test files matching pattern
python test_automation.py "test*.py" "Suite Name"

# Run specific test file
python test_automation.py "test_example.py"

# Run with default settings
python test_automation.py
```

## Best Practices

1. **Naming Conventions**: Use descriptive test names starting with `test_`
2. **Test Independence**: Each test should be independent and not rely on others
3. **Setup/Teardown**: Use setUp() and tearDown() for test fixtures
4. **Assertions**: Use appropriate assertions for better error messages
5. **Documentation**: Document test cases with docstrings

## Extending the Framework

### Adding Custom Assertions

```python
class MyTestCase(BaseTestCase):
    def assert_valid_email(self, email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        self.assertTrue(re.match(pattern, email), 
                       f"{email} is not a valid email")
```

### Adding Custom Test Runners

```python
from test_automation import TestAutomationFramework

class CustomTestRunner(TestAutomationFramework):
    def run_parallel_tests(self, test_suite):
        # Implement parallel test execution
        pass
```

## License

This project is licensed under the MIT License - see the licence.md file for details.
