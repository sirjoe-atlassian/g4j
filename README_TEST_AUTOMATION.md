# Test Automation Framework

## Overview
This test automation framework was generated for Jira issue DEV-4. It provides a simple yet extensible testing infrastructure for Python projects.

## Features

- **TestRunner**: A custom test runner for executing automated tests
- **TestResult**: Detailed test result tracking with timestamps
- **BaseTestCase**: Enhanced test case class with additional helper methods
- **Custom Assertions**: Extended assertion methods for common test scenarios
- **Comprehensive Reporting**: Detailed test execution summaries

## Usage

### Running the Example Tests

```bash
python3 test_automation.py
```

### Creating Custom Tests

```python
from test_automation import BaseTestCase, TestRunner
import unittest

class MyTests(BaseTestCase):
    """Your custom test cases."""
    
    def test_example(self):
        """Test description."""
        self.assertEqual(1 + 1, 2)
    
    def test_custom_assertion(self):
        """Test with custom assertions."""
        self.assert_between(5, 0, 10)
        self.assert_type("hello", str)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(MyTests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

### Using the TestRunner Directly

```python
from test_automation import TestRunner

def my_test():
    assert 2 + 2 == 4, "Math is broken!"

runner = TestRunner()
result = runner.run_test(my_test, "Addition Test")
runner.print_summary()
```

## Custom Assertions

The `BaseTestCase` class provides additional assertion methods:

- `assert_between(value, min_val, max_val, msg=None)`: Assert value is within range
- `assert_type(obj, expected_type, msg=None)`: Assert object type

## Test Results

Each test execution captures:
- Test name
- Pass/Fail status
- Error messages (if any)
- Timestamp
- Execution duration

## Requirements

- Python 3.6 or higher
- unittest module (standard library)

## License

This project is licensed under the MIT License - see the licence.md file for details.
