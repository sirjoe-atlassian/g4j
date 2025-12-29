# Test Automation Code Generator

A Python-based tool for automatically generating test code for functions, classes, and API endpoints.

## Features

- **Function Test Generation**: Automatically generate test cases for standalone functions
- **Class Test Generation**: Generate tests for class methods with initialization parameters
- **API Test Generation**: Create HTTP endpoint tests with various request methods
- **Multiple Framework Support**: Supports both pytest and unittest frameworks
- **Easy Configuration**: Simple API for defining test cases and expected results

## Installation

No external dependencies required for the core functionality. For API testing, install requests:

```bash
pip install requests pytest
```

## Usage

### Basic Function Testing

```python
from test_automation import TestCodeGenerator

# Create a generator instance
generator = TestCodeGenerator(test_framework="pytest")

# Define test cases
test_cases = [
    {'inputs': {'a': 1, 'b': 2}, 'expected': 3},
    {'inputs': {'a': 0, 'b': 0}, 'expected': 0},
]

# Generate test code
test_code = generator.generate_function_test(your_function, test_cases)
print(test_code)
```

### Class Testing

```python
# Define test cases for class methods
method_tests = {
    'add': [
        {'init_params': {'initial_value': 0}, 'inputs': {'x': 5}, 'expected': 5},
        {'init_params': {'initial_value': 10}, 'inputs': {'x': 3}, 'expected': 13},
    ],
    'subtract': [
        {'init_params': {'initial_value': 10}, 'inputs': {'x': 3}, 'expected': 7},
    ]
}

# Generate test code
test_code = generator.generate_class_test(YourClass, method_tests)
```

### API Testing

```python
# Define API test cases
api_test_cases = [
    {
        'headers': {'Content-Type': 'application/json'},
        'data': {'username': 'testuser', 'password': 'secret123'},
        'expected_status': 200,
        'expected_response': {'token': 'abc123', 'user_id': 1}
    }
]

# Generate API test code
test_code = generator.generate_api_test('/api/login', 'POST', api_test_cases)
```

### Save Tests to File

```python
# Save all generated tests
generator.save_tests('test_output.py')
```

## Test Case Format

### Function Tests
```python
{
    'inputs': {'param1': value1, 'param2': value2},  # Function parameters
    'expected': expected_result                        # Expected return value
}
```

### Class Method Tests
```python
{
    'init_params': {'param': value},  # Constructor parameters
    'inputs': {'param': value},        # Method parameters
    'expected': expected_result        # Expected return value
}
```

### API Tests
```python
{
    'headers': {'Header-Name': 'value'},    # HTTP headers
    'data': {'key': 'value'},                # Request data
    'expected_status': 200,                  # Expected HTTP status
    'expected_response': {'key': 'value'}    # Expected response body
}
```

## Supported Test Frameworks

- **pytest** (default): Modern, feature-rich testing framework
- **unittest**: Python's built-in testing framework

## Example Output

For a function `add_numbers(a, b)`, the generator creates:

```python
import pytest
from module import add_numbers

def test_add_numbers_1():
    result = add_numbers(a=1, b=2)
    assert result == 3

def test_add_numbers_2():
    result = add_numbers(a=0, b=0)
    assert result == 0
```

## Running the Demo

To see the test automation generator in action:

```bash
python tmp_rovodev_demo.py
```

This will generate example tests for functions, classes, and API endpoints.

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Future Enhancements

- Support for parameterized tests
- Mock object generation
- Test data generation from type hints
- Integration with code coverage tools
- Support for additional testing frameworks (nose2, doctest, etc.)
