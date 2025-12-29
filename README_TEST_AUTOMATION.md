# Test Automation Framework

A flexible and extensible Python test automation framework that provides enhanced testing capabilities beyond the standard unittest library.

## Features

- **Custom Test Logger**: Automatically logs test execution details to both file and console
- **Test Results Management**: Tracks and reports test results with detailed metrics
- **Enhanced Assertions**: Extended TestCase class with additional assertion methods
- **Data-Driven Testing**: Support for parameterized tests with multiple data sets
- **JSON Reporting**: Generates comprehensive test reports in JSON format
- **Zero External Dependencies**: Built entirely on Python standard library

## Project Structure

```
.
├── test_automation.py       # Main framework code
├── test_examples.py         # Example test cases demonstrating framework usage
├── requirements.txt         # Optional dependencies
├── licence.md              # MIT License
└── README_TEST_AUTOMATION.md # This file
```

## Installation

No installation required! The framework uses only Python standard library components.

For optional enhanced features, install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Test Execution

Run the example tests:
```bash
python3 test_automation.py      # Run basic framework examples
python3 test_examples.py        # Run comprehensive test suite
```

### Creating Custom Tests

```python
from test_automation import TestCase, TestRunner, TestLogger

class MyCustomTest(TestCase):
    def test_example(self):
        """Example test method."""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_custom_assertion(self):
        """Test with custom assertion."""
        value = 75
        self.assertBetween(value, 0, 100)

# Run the tests
if __name__ == "__main__":
    import unittest
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(MyCustomTest)
    
    logger = TestLogger("my_tests.log")
    runner = TestRunner(logger)
    runner.run_test_suite(suite)
    runner.generate_report("my_test_report.json")
```

### Data-Driven Testing

```python
from test_automation import DataDrivenTest, TestRunner, TestLogger

def test_function(a, b, expected):
    """Parameterized test function."""
    result = a + b
    assert result == expected, f"Expected {expected}, got {result}"

# Define test data
test_data = [
    {"a": 1, "b": 1, "expected": 2},
    {"a": 5, "b": 5, "expected": 10},
    {"a": -3, "b": 7, "expected": 4},
]

# Execute data-driven test
logger = TestLogger()
runner = TestRunner(logger)
ddt = DataDrivenTest(test_function, test_data)
results = ddt.run(runner)
runner.generate_report("ddt_report.json")
```

## Framework Components

### TestLogger
Provides logging functionality for test execution:
- Logs to both file and console
- Tracks test start, end, and errors
- Configurable log file location

### TestResult
Represents individual test results:
- Test name
- Status (passed, failed, skipped, error)
- Duration
- Error messages
- Timestamp

### TestRunner
Orchestrates test execution:
- Runs individual test functions
- Runs unittest TestSuite
- Generates JSON reports
- Tracks all test results

### TestCase
Extended unittest.TestCase with additional assertions:
- `assertBetween(value, min, max)` - Assert value is within range
- `assertResponse(response, status_code)` - Assert HTTP response status
- `assertContainsKey(dict, key)` - Assert dictionary contains key

### DataDrivenTest
Enables parameterized testing:
- Run same test with multiple data sets
- Automatic test naming
- Individual result tracking per data set

## Test Reports

The framework generates JSON reports with the following structure:

```json
{
  "total_tests": 4,
  "passed": 4,
  "failed": 0,
  "errors": 0,
  "skipped": 0,
  "results": [
    {
      "test_name": "test_addition",
      "status": "passed",
      "duration": 0.0001,
      "error_message": null,
      "timestamp": "2024-12-29T04:10:45.882000"
    }
  ]
}
```

## Example Test Results

Running the included examples produces:

**Basic Framework Tests** (`test_automation.py`):
- 4 tests executed
- All tests passed
- Report: `example_test_report.json`

**Comprehensive Test Suite** (`test_examples.py`):
- 23 unit tests
- 5 data-driven tests
- Multiple test categories: Math, String, List, Dictionary operations
- Reports: `test_examples_report.json`, `data_driven_report.json`

## Log Files

The framework generates detailed log files:
- `automation_tests.log` - Basic framework test logs
- `test_examples.log` - Comprehensive test suite logs
- `data_driven_test.log` - Data-driven test logs

## Requirements

- Python 3.6 or higher
- No external dependencies required for core functionality

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

Contributions are welcome! The framework is designed to be extensible. Consider adding:
- Additional custom assertions
- More test result formats (HTML, XML)
- Test discovery utilities
- Parallel test execution
- Test fixtures and setup helpers

## Future Enhancements

Potential areas for expansion:
- Integration with pytest
- HTML report generation
- Code coverage integration
- Test result visualization
- CI/CD integration examples
- Mock object utilities
- API testing helpers
- Performance testing capabilities

## Contact

For questions, issues, or contributions related to this test automation framework, please refer to the project repository.
