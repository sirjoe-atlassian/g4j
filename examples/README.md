# Test Generator Examples

This directory contains sample code and generated tests to demonstrate the test generator's capabilities.

## Files

### sample_calculator.py
A simple Calculator class with basic arithmetic operations (add, subtract, multiply, divide).

### test_calculator.py
Generated pytest tests for the Calculator class. To run these tests:

```bash
# Install pytest if not already installed
pip install pytest

# Run the tests (they will fail initially as they need implementation)
pytest test_calculator.py -v
```

## Implementing the Generated Tests

The generated tests provide a skeleton with TODOs. Here's an example of how to implement one:

### Before (Generated):
```python
def test_add(calculator_instance):
    """
    Test the add method.
    
    TODO: Implement test logic
    """
    # Arrange
    # TODO: Set up test data and expectations
    
    # Act
    # result = calculator_instance.add()
    
    # Assert
    # assert result == expected_value
    pytest.fail('Test not implemented')
```

### After (Implemented):
```python
def test_add(calculator_instance):
    """
    Test the add method.
    """
    # Arrange
    a = 5
    b = 3
    expected = 8
    
    # Act
    result = calculator_instance.add(a, b)
    
    # Assert
    assert result == expected
```

## Try It Yourself

Generate more test examples:

```bash
# From the examples directory
python ../test_generator.py --framework pytest --language python --class-name Calculator --methods add subtract multiply divide --output test_calculator_custom.py
```
