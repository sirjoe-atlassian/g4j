# Test Automation Framework

A simple and flexible test automation framework for Python projects.

## Overview

This test automation framework provides a lightweight solution for writing and running automated tests. It includes:

- **test_automation.py**: Core framework with test registration, execution, and reporting
- **test_automation_example.py**: Example implementation showing how to use the framework

## Features

- ✅ Simple test registration and execution
- ✅ Setup and teardown hooks for each test
- ✅ Detailed test results with duration tracking
- ✅ Clear pass/fail reporting with error messages
- ✅ Summary statistics for test runs
- ✅ Exception handling and assertion support

## Installation

No external dependencies required! Just Python 3.6+

```bash
# Copy the test_automation.py file to your project
cp test_automation.py /path/to/your/project/
```

## Quick Start

### Basic Usage

```python
from test_automation import TestAutomation

# Create automation instance
automation = TestAutomation()

# Define your test
def test_something():
    assert 1 + 1 == 2

# Register and run
automation.register_test("My Test", test_something)
automation.run_all_tests()
```

### With Setup and Teardown

```python
from test_automation import TestAutomation

automation = TestAutomation()

# Define setup/teardown
def setup():
    print("Preparing test environment...")

def teardown():
    print("Cleaning up...")

automation.set_setup(setup)
automation.set_teardown(teardown)

# Register tests
def test_feature():
    assert True

automation.register_test("Feature Test", test_feature)
automation.run_all_tests()
```

## Example Output

```
============================================================
Running 5 test(s)...
============================================================

  [Setup] Preparing test environment...
  [Teardown] Cleaning up...
Test: Addition Tests - PASSED (Duration: 0.001s)
  [Setup] Preparing test environment...
  [Teardown] Cleaning up...
Test: Subtraction Tests - PASSED (Duration: 0.000s)
...

============================================================
Test Summary:
  Total: 5
  Passed: 5
  Failed: 0
  Total Duration: 0.003s
============================================================
```

## API Reference

### TestAutomation Class

#### Methods

- `register_test(name: str, test_func: Callable)` - Register a test function
- `set_setup(setup_func: Callable)` - Set setup function to run before each test
- `set_teardown(teardown_func: Callable)` - Set teardown function to run after each test
- `run_all_tests() -> List[TestResult]` - Execute all registered tests
- `run_test(name: str, test_func: Callable) -> TestResult` - Run a single test
- `get_results() -> List[TestResult]` - Get results of executed tests

### TestResult Class

Represents the result of a test execution.

#### Attributes

- `test_name: str` - Name of the test
- `passed: bool` - Whether the test passed
- `duration: float` - Execution time in seconds
- `error_message: str` - Error message if test failed (None if passed)

## Running Examples

### Run the built-in example

```bash
python3 test_automation.py
```

### Run the calculator example

```bash
python3 test_automation_example.py
```

## Use Cases

- Unit testing for Python applications
- Integration testing
- API testing
- Data validation testing
- Regression testing
- Smoke testing

## Best Practices

1. **Keep tests independent** - Each test should run independently of others
2. **Use descriptive test names** - Make it clear what each test is validating
3. **One assertion per test** - Or group related assertions together
4. **Use setup/teardown** - For common initialization and cleanup tasks
5. **Handle exceptions** - The framework catches exceptions, but design tests to be explicit

## Contributing

This is a basic framework that can be extended based on your needs. Feel free to:

- Add parallel test execution
- Implement test fixtures
- Add support for test parametrization
- Create custom assertions
- Add HTML/XML report generation
- Integrate with CI/CD pipelines

## License

See licence.md for licensing information.

## Related Jira Issues

- DEV-4: Test automation generate code
- DEV-2: Task 2 (Parent task)
