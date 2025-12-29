# Test Automation Code Generator

A Python-based test automation code generator that creates test cases from specifications.

## Features

- Generate test cases for multiple frameworks (pytest, unittest)
- Support for JSON-based test specifications
- Automatic test file creation and organization
- Follows AAA (Arrange-Act-Assert) pattern
- Extensible architecture for additional frameworks

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd g4j

# No additional dependencies required for basic usage
# For pytest support:
pip install pytest
```

## Usage

### Basic Usage

```python
from test_generator import TestGenerator

# Create a test generator instance
generator = TestGenerator(framework="pytest")

# Define test cases
test_cases = [
    {
        "name": "addition",
        "description": "Test basic addition operation",
        "inputs": {"a": 2, "b": 3},
        "expected": 5
    },
    {
        "name": "subtraction",
        "description": "Test basic subtraction operation",
        "inputs": {"a": 5, "b": 3},
        "expected": 2
    }
]

# Generate test code
test_code = generator.generate_test_class("TestMathOperations", test_cases)

# Save to file
generator.save_test_file(test_code, "test_math_operations.py")
```

### Using JSON Specifications

```python
from test_generator import TestGenerator
import json

# Define test specification in JSON
spec = {
    "class_name": "TestUserAuthentication",
    "test_cases": [
        {
            "name": "valid_login",
            "description": "Test login with valid credentials",
            "inputs": {
                "username": "testuser",
                "password": "password123"
            },
            "expected": True
        },
        {
            "name": "invalid_login",
            "description": "Test login with invalid credentials",
            "inputs": {
                "username": "testuser",
                "password": "wrongpassword"
            },
            "expected": False
        }
    ]
}

# Generate from JSON
generator = TestGenerator(framework="pytest")
test_code = generator.generate_from_json(json.dumps(spec))
print(test_code)
```

### Running the Example

```bash
# Run the built-in example
python test_generator.py
```

## Supported Frameworks

- **pytest**: Modern Python testing framework
- **unittest**: Python's built-in testing framework

## Test Specification Format

Test specifications should follow this JSON structure:

```json
{
    "class_name": "TestClassName",
    "test_cases": [
        {
            "name": "test_case_name",
            "description": "Description of what this test does",
            "inputs": {
                "param1": "value1",
                "param2": "value2"
            },
            "expected": "expected_result"
        }
    ]
}
```

### Fields:

- `class_name`: Name of the generated test class
- `test_cases`: Array of test case specifications
  - `name`: Test method name (will be prefixed with `test_`)
  - `description`: Optional description for the test
  - `inputs`: Dictionary of input parameters for the test
  - `expected`: Expected result for assertions

## Generated Test Structure

The generator creates tests following the AAA pattern:

```python
def test_example(self):
    """Test description"""
    # Arrange
    input1 = "value1"
    input2 = "value2"
    
    # Act
    result = function_under_test(input1, input2)
    
    # Assert
    assert result == expected_value
```

## Output Directory

By default, generated test files are saved to the `tests/` directory. You can customize this:

```python
generator.save_test_file(test_code, "my_test.py", output_dir="custom_tests")
```

## Examples

### Pytest Example Output

```python
import pytest


class TestMathOperations:
    """Generated test class for TestMathOperations"""

    def test_addition(self):
        """Test basic addition operation"""
        # Arrange
        a = 2
        b = 3

        # Act
        # TODO: Add your test logic here
        result = None  # Replace with actual function call

        # Assert
        assert result == 5
```

### Unittest Example Output

```python
import unittest


class TestMathOperations(unittest.TestCase):
    """Generated test class for TestMathOperations"""

    def test_addition(self):
        """Test basic addition operation"""
        # Arrange
        a = 2
        b = 3

        # Act
        # TODO: Add your test logic here
        result = None  # Replace with actual function call

        # Assert
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
```

## Extending the Generator

To add support for additional testing frameworks:

1. Add a new method like `_generate_<framework>_class()`
2. Update the `generate_test_class()` method to support the new framework
3. Implement the framework-specific test generation logic

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
