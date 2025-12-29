# Test Automation Framework

**Generated for Jira Issue:** DEV-4 - Test automation generate code

## Overview

This test automation framework provides a comprehensive solution for creating, executing, and reporting on automated tests. It includes test case management, custom assertions, and flexible reporting capabilities.

## Features

- **Test Case Management**: Create and organize test cases with metadata
- **Test Suite Execution**: Group and run multiple test cases together
- **Custom Assertions**: Extended assertion methods for common validation scenarios
- **Result Reporting**: Generate HTML reports with detailed test results
- **Tag-based Filtering**: Filter tests by tags for selective execution
- **Performance Testing**: Built-in assertions for response time validation

## Installation

No external dependencies required for the core framework. Uses only Python standard library.

For running the unit tests:
```bash
python -m pytest tests/
# or
python -m unittest discover tests/
```

## Quick Start

### Basic Example

```python
from test_automation import TestCase, TestSuite

# Create a test suite
suite = TestSuite("My Test Suite", "Testing my application")

# Create a test case
test = TestCase(
    "test_example",
    "Verify basic functionality",
    ["smoke", "critical"]
)

# Define test function
def my_test():
    assert 1 + 1 == 2

# Execute the test
test.execute(my_test)
suite.add_test(test)

# Run the suite
suite.run()
print(suite.get_summary())
```

### Using Custom Assertions

```python
from test_automation import CustomAssertions

# Validate value ranges
CustomAssertions.assert_in_range(25, 1, 100)

# Validate dictionary structure
user_data = {"id": 1, "name": "John"}
CustomAssertions.assert_dict_contains(user_data, ["id", "name"])

# Validate list contents
permissions = ["read", "write", "delete"]
CustomAssertions.assert_list_contains(permissions, ["read", "write"])

# Validate response times
CustomAssertions.assert_response_time(0.5, 1.0)  # 0.5s actual, 1.0s max
```

## File Structure

```
.
├── test_automation.py          # Core framework implementation
├── test_automation_example.py  # Example usage and test cases
├── tests/
│   └── test_automation_tests.py  # Unit tests for the framework
├── README_TEST_AUTOMATION.md   # This file
└── licence.md                  # MIT License
```

## Core Components

### TestCase

Represents a single test with execution tracking.

**Attributes:**
- `name`: Test case name
- `description`: What the test validates
- `tags`: List of categorization tags
- `result`: TestResult enum (PASSED/FAILED/SKIPPED/ERROR)
- `duration`: Execution time in seconds
- `error_message`: Error details if test failed

**Methods:**
- `execute(test_function)`: Run the test function
- `to_dict()`: Convert to dictionary representation

### TestSuite

Manages a collection of test cases.

**Methods:**
- `add_test(test_case)`: Add a test to the suite
- `run(tag_filter)`: Execute all tests (optionally filtered by tags)
- `get_summary()`: Get formatted text summary

### CustomAssertions

Static methods for common validation patterns.

**Methods:**
- `assert_in_range(value, min_val, max_val)`: Validate numeric ranges
- `assert_dict_contains(dictionary, expected_keys)`: Validate dictionary structure
- `assert_list_contains(lst, expected_items)`: Validate list contents
- `assert_response_time(duration, max_duration)`: Validate performance

### TestReporter

Generate test execution reports.

**Methods:**
- `generate_html_report(test_suite, output_path)`: Create HTML report

## Running Examples

### Run the example test suite:
```bash
python test_automation_example.py
```

This will:
1. Execute several example test cases
2. Print results to console
3. Generate `test_report.html`

### Run framework unit tests:
```bash
python -m unittest tests/test_automation_tests.py
```

## Advanced Usage

### Tag-based Test Filtering

```python
# Create tests with different tags
test1 = TestCase("test_api", "API test", ["api", "integration"])
test2 = TestCase("test_ui", "UI test", ["ui", "integration"])
test3 = TestCase("test_unit", "Unit test", ["unit"])

suite.add_test(test1)
suite.add_test(test2)
suite.add_test(test3)

# Run only integration tests
suite.run(tag_filter=["integration"])
```

### Generating Reports

```python
from test_automation import TestReporter

# After running tests
TestReporter.generate_html_report(suite, "reports/test_results.html")
```

### Performance Testing

```python
import time

def performance_test():
    start = time.time()
    # Your code to test
    do_something()
    duration = time.time() - start
    
    # Assert it completed within 2 seconds
    CustomAssertions.assert_response_time(duration, 2.0)

test = TestCase("test_performance", "Check operation speed", ["performance"])
test.execute(performance_test)
```

## Test Results

Test results are tracked with the following enum values:

- `PASSED`: Test executed successfully with no assertions failed
- `FAILED`: Test failed due to assertion error
- `ERROR`: Test encountered an unexpected exception
- `SKIPPED`: Test was not executed (e.g., filtered by tags)

## Best Practices

1. **Use descriptive names**: Make test names and descriptions clear
2. **Tag appropriately**: Use tags for organizing tests by type/priority
3. **Keep tests independent**: Each test should run independently
4. **Use custom assertions**: Leverage custom assertions for clarity
5. **Monitor performance**: Use response time assertions for critical paths
6. **Generate reports**: Always generate reports for test runs

## Extending the Framework

The framework is designed to be extensible:

### Add Custom Assertions

```python
class CustomAssertions:
    @staticmethod
    def assert_email_valid(email: str):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise AssertionError(f"Invalid email format: {email}")
```

### Create Custom Reporters

```python
class CustomReporter:
    @staticmethod
    def generate_json_report(test_suite, output_path):
        import json
        report_data = {
            "suite": test_suite.name,
            "tests": [tc.to_dict() for tc in test_suite.test_cases]
        }
        with open(output_path, 'w') as f:
            json.dump(report_data, f, indent=2)
```

## License

This project is licensed under the MIT License - see the `licence.md` file for details.

## Related Jira Issues

- **DEV-4**: Test automation generate code (This implementation)
- **DEV-2**: Task 2 (Parent task)

## Support

For issues or questions related to this framework, please refer to the Jira project.
