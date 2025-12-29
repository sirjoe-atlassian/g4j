# Test Automation Framework

This test automation framework was generated for **Jira Issue DEV-4: Test automation generate code**.

## Overview

A flexible and extensible Python-based test automation framework that supports:
- Unit testing
- Integration testing
- End-to-end (E2E) testing
- Comprehensive test reporting
- Configurable test execution
- Setup and teardown hooks

## Project Structure

```
.
├── licence.md                  # MIT License
├── test_automation.py          # Main test automation framework
├── test_config.json            # Configuration file for test settings
├── requirements.txt            # Python dependencies
└── README_TEST_AUTOMATION.md   # This file
```

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

### Running the Sample Tests

The framework includes sample tests to demonstrate functionality:

```bash
python test_automation.py
```

This will:
- Execute the sample test suite
- Display test results in the console
- Generate a `test_report.json` file with detailed results

### Using the Framework

#### Basic Test Example

```python
from test_automation import TestCase, TestRunner

class MyTests(TestCase):
    def test_example(self):
        """Example test case."""
        result = 10 + 5
        self.assertEqual(result, 15)
    
    def test_string(self):
        """Test string operations."""
        text = "automation"
        self.assertIn("auto", text)

# Run the tests
if __name__ == '__main__':
    runner = TestRunner()
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    runner.run_test_suite(suite)
    runner.print_summary()
```

#### Custom Test Functions

```python
from test_automation import TestRunner

def my_custom_test():
    """A custom test function."""
    assert 2 + 2 == 4, "Math is broken!"

runner = TestRunner()
runner.run_test(my_custom_test)
runner.print_summary()
```

#### Setup and Teardown Hooks

```python
runner = TestRunner()

# Add setup hook
runner.add_setup_hook(lambda: print("Setting up test environment..."))

# Add teardown hook
runner.add_teardown_hook(lambda: print("Cleaning up..."))

runner.run_setup()
# ... run tests ...
runner.run_teardown()
```

## Configuration

The framework uses `test_config.json` for configuration:

```json
{
  "test_automation": {
    "settings": {
      "log_level": "INFO",
      "report_format": "json",
      "output_directory": "./test_reports"
    },
    "test_suites": {
      "unit_tests": {
        "enabled": true,
        "path": "./tests/unit",
        "pattern": "test_*.py"
      }
    }
  }
}
```

### Configuration Options

- **log_level**: Logging verbosity (DEBUG, INFO, WARNING, ERROR)
- **report_format**: Output format for test reports (json, html, xml)
- **output_directory**: Directory for test reports
- **retry_failed_tests**: Enable automatic retry of failed tests
- **parallel_execution**: Run tests in parallel

## Features

### TestRunner Class

The main test execution engine with methods:
- `run_test(test_func, test_name)` - Run a single test function
- `run_test_suite(test_suite)` - Run a unittest TestSuite
- `add_setup_hook(hook)` - Add pre-test setup logic
- `add_teardown_hook(hook)` - Add post-test cleanup logic
- `generate_report()` - Generate comprehensive test report
- `save_report(filename)` - Save report to JSON file
- `print_summary()` - Display test results summary

### TestCase Class

Extended unittest.TestCase with additional assertions:
- `assert_in_range(value, min_val, max_val)` - Assert value is within range
- `assert_json_equal(actual, expected)` - Assert JSON objects match

### TestResult Class

Captures detailed test execution information:
- Test name
- Status (PASSED, FAILED, SKIPPED, ERROR)
- Duration
- Error messages
- Timestamp

## Test Report Format

The framework generates JSON reports with the following structure:

```json
{
  "summary": {
    "total_tests": 4,
    "passed": 4,
    "failed": 0,
    "errors": 0,
    "skipped": 0,
    "success_rate": 100.0,
    "total_duration": 0.002
  },
  "results": [
    {
      "test_name": "test_addition",
      "status": "PASSED",
      "duration": 0.001,
      "message": "Test passed successfully",
      "error": null,
      "timestamp": "2024-01-01T12:00:00.000000"
    }
  ]
}
```

## Best Practices

1. **Organize tests by type**: Separate unit, integration, and E2E tests
2. **Use descriptive test names**: Make test purposes clear
3. **Keep tests independent**: Tests should not depend on each other
4. **Use setup/teardown**: Clean up resources after tests
5. **Assert clearly**: Use appropriate assertion methods
6. **Document tests**: Add docstrings to test methods

## Extending the Framework

### Adding Custom Assertions

```python
class MyTestCase(TestCase):
    def assert_response_ok(self, response):
        """Custom assertion for HTTP responses."""
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
```

### Adding Test Fixtures

```python
class MyTests(TestCase):
    def setUp(self):
        """Run before each test."""
        self.test_data = {"key": "value"}
    
    def tearDown(self):
        """Run after each test."""
        self.test_data = None
```

## Integration with CI/CD

The framework can be integrated with CI/CD pipelines:

```bash
# Run tests and generate report
python test_automation.py

# Check exit code for pass/fail
if [ $? -eq 0 ]; then
    echo "Tests passed!"
else
    echo "Tests failed!"
    exit 1
fi
```

## Dependencies

See `requirements.txt` for the full list of dependencies:
- pytest: Advanced testing framework
- pytest-cov: Code coverage reports
- pytest-html: HTML test reports
- requests: HTTP client for API testing
- faker: Generate test data

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Support

For issues related to Jira task DEV-4, please refer to:
- Jira Issue: [DEV-4](https://jyang4-test.atlassian.net/browse/DEV-4)
- Parent Task: DEV-2

## Contributing

When contributing to this framework:
1. Write tests for new features
2. Maintain backward compatibility
3. Update documentation
4. Follow PEP 8 style guidelines
5. Add type hints where appropriate

## Roadmap

Future enhancements:
- [ ] HTML report generation
- [ ] Parallel test execution
- [ ] Integration with popular CI/CD tools
- [ ] API testing utilities
- [ ] Database testing utilities
- [ ] Performance testing capabilities
- [ ] Screenshot capture for UI tests
- [ ] Test data management
- [ ] Mock and stub utilities
