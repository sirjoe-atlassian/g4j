# Test Automation Framework

A comprehensive Python-based test automation framework for generating and executing automated tests.

## Features

- **Flexible Test Case Creation**: Create test cases with setup, test steps, and teardown phases
- **Test Suite Management**: Organize multiple test cases into test suites
- **Test Generators**: Automatically generate tests for APIs, unit tests, and integration tests
- **Result Tracking**: Track test execution results with detailed status and timing information
- **JSON Export**: Export test results to JSON format for reporting and analysis
- **Extensible Architecture**: Easy to extend with custom test types and assertions

## Installation

No external dependencies required - uses Python standard library only.

```bash
# Clone the repository
git clone <repository-url>
cd g4j

# Run the demo
python test_automation_framework.py
```

## Quick Start

### Basic Test Case

```python
from test_automation_framework import TestCase, TestSuite

# Create a test case
test = TestCase("test_example", "Example test case")
test.add_setup(lambda: print("Setting up"))
test.add_test_step(lambda: print("Running test"))
test.add_teardown(lambda: print("Cleaning up"))

# Create a test suite and add the test
suite = TestSuite("My Test Suite")
suite.add_test(test)

# Run the suite
results = suite.run()

# Export results
suite.export_results("results.json")
```

### Using Test Generators

```python
from test_automation_framework import TestGenerator, TestSuite

suite = TestSuite("Generated Tests")

# Generate API test
api_test = TestGenerator.generate_api_test("/api/users", "GET", 200)
suite.add_test(api_test)

# Generate unit test
unit_test = TestGenerator.generate_unit_test("add", [2, 3], 5)
suite.add_test(unit_test)

# Generate integration test
integration_test = TestGenerator.generate_integration_test("Database", "API")
suite.add_test(integration_test)

# Run all tests
suite.run()
```

## Examples

See `test_examples.py` for comprehensive examples including:

- Calculator tests
- User management tests
- API integration tests
- Database operation tests
- Component integration tests

Run examples:

```bash
python test_examples.py
```

## Architecture

### Core Components

1. **TestCase**: Represents a single test with setup, execution, and teardown phases
2. **TestSuite**: Collection of test cases that can be executed together
3. **TestResult**: Data structure storing test execution results
4. **TestGenerator**: Utility for programmatically generating test cases
5. **TestStatus**: Enumeration of possible test states (PASSED, FAILED, ERROR, SKIPPED)

### Test Execution Flow

1. **Setup Phase**: Execute all setup actions
2. **Test Phase**: Execute all test steps
3. **Teardown Phase**: Execute all teardown actions (always runs)
4. **Result Collection**: Capture status, duration, and any error messages

## Extending the Framework

### Custom Test Types

```python
class CustomTestGenerator:
    @staticmethod
    def generate_custom_test(param1, param2):
        test = TestCase(f"test_custom_{param1}", f"Custom test for {param1}")
        
        def custom_logic():
            # Your custom test logic here
            pass
        
        test.add_test_step(custom_logic)
        return test
```

### Custom Assertions

```python
def assert_response_time(response, max_time):
    if response.duration > max_time:
        raise AssertionError(f"Response time {response.duration}s exceeds {max_time}s")

test = TestCase("test_performance", "Performance test")
test.add_test_step(lambda: assert_response_time(make_request(), 1.0))
```

## Test Result Format

Test results are exported in JSON format:

```json
{
  "suite_name": "Example Suite",
  "total_tests": 3,
  "timestamp": "2025-12-29T12:00:00.000000",
  "results": [
    {
      "test_name": "test_example",
      "status": "PASSED",
      "duration": 0.0123,
      "error_message": "",
      "timestamp": "2025-12-29T12:00:00.000000"
    }
  ]
}
```

## Best Practices

1. **Use descriptive test names**: Name tests clearly to understand their purpose
2. **Keep tests independent**: Each test should be able to run in isolation
3. **Clean up resources**: Always use teardown to clean up test resources
4. **Use test generators**: For repetitive test patterns, create generators
5. **Export results**: Save test results for tracking and analysis
6. **Organize into suites**: Group related tests into logical suites

## Contributing

Contributions are welcome! Please ensure:

- Tests are well-documented
- Code follows Python best practices
- New features include examples
- All tests pass before submitting

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Future Enhancements

- [ ] Parallel test execution
- [ ] HTML report generation
- [ ] Test retry mechanism
- [ ] Test dependency management
- [ ] CI/CD integration templates
- [ ] Performance benchmarking
- [ ] Screenshot capture for UI tests
- [ ] Database fixtures and mocking
