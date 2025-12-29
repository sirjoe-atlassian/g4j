# Test Automation Code Generator

A Python tool that automatically generates test code for your Python functions and classes.

## Features

- **Automatic Test Generation**: Generates test cases from Python source code
- **Multiple Framework Support**: Supports both pytest and unittest frameworks
- **Smart Parameter Inference**: Attempts to infer appropriate test data based on parameter names
- **Class and Function Support**: Handles both standalone functions and class methods
- **AAA Pattern**: Generated tests follow the Arrange-Act-Assert pattern
- **Extensible**: Easy to customize and extend for specific needs

## Installation

No external dependencies required! Uses only Python standard library plus pytest or unittest for running tests.

```bash
# For pytest support
pip install pytest

# No additional installation needed for unittest (part of standard library)
```

## Usage

### Command Line Usage

Generate tests from a source file:

```bash
# Generate pytest tests (default)
python test_generator.py my_module.py

# Generate unittest tests
python test_generator.py my_module.py test_my_module.py unittest

# Specify custom output file
python test_generator.py my_module.py tests/test_custom.py pytest
```

### Programmatic Usage

```python
from test_generator import TestCodeGenerator, generate_test_file

# Generate tests for a file
generate_test_file('my_module.py', 'test_my_module.py', framework='pytest')

# Or use the class directly
generator = TestCodeGenerator(framework='pytest')

# Generate from source code string
source_code = '''
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(x, y):
    """Multiply two numbers."""
    return x * y
'''

test_code = generator.generate_test_from_source(source_code, 'my_module')
print(test_code)

# Generate tests for a specific function
def my_function(param1, param2):
    return param1 + param2

test_code = generator.generate_test_for_function(my_function)
print(test_code)
```

## Example

### Input (calculator.py):

```python
def add(a, b):
    """Add two numbers together."""
    return a + b

def divide(numerator, denominator):
    """Divide two numbers."""
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator

class Calculator:
    """A simple calculator class."""
    
    def calculate(self, operation, x, y):
        """Perform a calculation."""
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        return None
```

### Output (pytest format):

```python
import pytest
from calculator import *


def test_add_basic():
    """Test basic functionality of add."""
    # Arrange
    a = 1
    b = 1
    
    # Act
    result = add(a, b)
    
    # Assert
    assert result is not None
    # TODO: Add specific assertions


def test_add_edge_cases():
    """Test edge cases for add."""
    # TODO: Implement edge case tests
    pass


def test_add_invalid_input():
    """Test add with invalid input."""
    # TODO: Test error handling
    pass


# Tests for Calculator class

class TestCalculator:
    """Test suite for Calculator class."""
    
    @pytest.fixture
    def instance(self):
        """Create a Calculator instance for testing."""
        return Calculator()
    
    def test_calculate(self, instance):
        """Test calculate method."""
        # Arrange
        operation = "test"
        x = 1
        y = 1
        
        # Act
        result = instance.calculate(operation, x, y)
        
        # Assert
        assert result is not None
        # TODO: Add specific assertions
```

## Generated Test Structure

The generator creates:

1. **Basic functionality tests**: Verify the function/method works with typical inputs
2. **Edge case tests**: Placeholders for testing boundary conditions
3. **Invalid input tests**: Placeholders for error handling tests
4. **Fixtures/Setup**: Proper test fixtures for class instances

## Customization

The test generator uses naming conventions to infer appropriate test data:

- Parameters with 'count', 'num', 'size', 'index' → integer values
- Parameters with 'name', 'text', 'str', 'msg' → string values
- Parameters with 'list', 'items', 'array' → empty lists
- Parameters with 'dict', 'map', 'config' → empty dictionaries
- Parameters with 'flag', 'is_', 'has_', 'enabled' → boolean values

## Best Practices

1. **Review Generated Tests**: Always review and enhance generated tests
2. **Add Specific Assertions**: Replace generic assertions with specific checks
3. **Implement Edge Cases**: Fill in the edge case test placeholders
4. **Test Error Handling**: Add proper exception testing where needed
5. **Add Test Data**: Provide realistic test data for better coverage

## License

This project is licensed under the MIT License - see the licence.md file for details.

## Contributing

Contributions are welcome! Some areas for improvement:

- Add support for more testing frameworks (nose2, etc.)
- Improve parameter type inference
- Generate mock objects for dependencies
- Add coverage analysis
- Support for async functions
- Type hint analysis for better test data generation
