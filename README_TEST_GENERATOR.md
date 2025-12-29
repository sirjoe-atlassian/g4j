# Test Automation Code Generator

A flexible tool for automatically generating test automation code for various testing frameworks and programming languages.

## Features

- **Multiple Framework Support**: Generate tests for pytest, unittest, Jest, and JUnit
- **Multi-Language**: Supports Python, JavaScript, and Java
- **Boilerplate Generation**: Automatically creates test structure with proper imports, fixtures, and test methods
- **CLI Interface**: Easy-to-use command-line interface
- **Customizable Output**: Generate to stdout or save directly to files

## Supported Frameworks

| Language   | Frameworks        |
|------------|-------------------|
| Python     | pytest, unittest  |
| JavaScript | Jest              |
| Java       | JUnit             |

## Installation

```bash
# Make the script executable (optional)
chmod +x test_generator.py
```

## Usage

### Command Line Interface

```bash
python test_generator.py --framework <framework> --language <language> --class-name <ClassName> --methods <method1> <method2> ... [--output <file>]
```

### Examples

#### Generate pytest tests for a Python class

```bash
python test_generator.py \
  --framework pytest \
  --language python \
  --class-name Calculator \
  --methods add subtract multiply divide \
  --output tests/test_calculator.py
```

#### Generate unittest tests

```bash
python test_generator.py \
  --framework unittest \
  --language python \
  --class-name UserService \
  --methods create_user delete_user update_user get_user \
  --output tests/test_user_service.py
```

#### Generate Jest tests for JavaScript

```bash
python test_generator.py \
  --framework jest \
  --language javascript \
  --class-name ShoppingCart \
  --methods addItem removeItem getTotal \
  --output tests/ShoppingCart.test.js
```

#### Generate JUnit tests for Java

```bash
python test_generator.py \
  --framework junit \
  --language java \
  --class-name OrderProcessor \
  --methods processOrder cancelOrder refundOrder \
  --output tests/OrderProcessorTest.java
```

#### Print to stdout (no output file)

```bash
python test_generator.py \
  --framework pytest \
  --language python \
  --class-name Example \
  --methods test_method
```

## Programmatic Usage

You can also use the `TestGenerator` class directly in your Python code:

```python
from test_generator import TestGenerator, TestFramework, Language

# Create a generator instance
generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)

# Generate test code
test_code = generator.generate_test_file(
    class_name="Calculator",
    methods=["add", "subtract", "multiply", "divide"],
    output_path="tests/test_calculator.py"
)

print(test_code)
```

## Generated Test Structure

### pytest Example

```python
import pytest
from calculator import Calculator

@pytest.fixture
def calculator_instance():
    """Fixture to create a Calculator instance."""
    return Calculator()

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

### unittest Example

```python
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator."""

    def setUp(self):
        """Set up test fixtures."""
        self.instance = Calculator()

    def test_add(self):
        """
        Test the add method.
        
        TODO: Implement test logic
        """
        # Arrange
        # TODO: Set up test data and expectations
        
        # Act
        # result = self.instance.add()
        
        # Assert
        # self.assertEqual(result, expected_value)
        self.fail('Test not implemented')

if __name__ == "__main__":
    unittest.main()
```

### Jest Example

```javascript
const Calculator = require('./calculator');

describe('Calculator', () => {
  let instance;

  beforeEach(() => {
    instance = new Calculator();
  });

  test('add should work correctly', () => {
    // Arrange
    // TODO: Set up test data and expectations
    
    // Act
    // const result = instance.add();
    
    // Assert
    // expect(result).toBe(expectedValue);
    fail('Test not implemented');
  });
});
```

### JUnit Example

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    private Calculator instance;

    @BeforeEach
    public void setUp() {
        instance = new Calculator();
    }

    @Test
    public void testAdd() {
        // Arrange
        // TODO: Set up test data and expectations
        
        // Act
        // ResultType result = instance.add();
        
        // Assert
        // assertEquals(expectedValue, result);
        fail("Test not implemented");
    }
}
```

## Test Structure Pattern

All generated tests follow the Arrange-Act-Assert (AAA) pattern:

1. **Arrange**: Set up test data and expectations
2. **Act**: Execute the method being tested
3. **Assert**: Verify the results

This structure provides a clear template that developers can fill in with actual test logic.

## Requirements

- Python 3.6 or higher
- No external dependencies for the generator itself
- Target test frameworks must be installed separately:
  - `pytest` for pytest tests
  - Built-in `unittest` for unittest tests
  - `jest` for Jest tests
  - `junit` for JUnit tests

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to add support for additional frameworks or languages.

## Roadmap

Future enhancements may include:

- Support for more testing frameworks (Mocha, Jasmine, TestNG, etc.)
- Additional languages (TypeScript, C#, Go, etc.)
- Test data generation
- Mock/stub generation
- Integration with CI/CD pipelines
- IDE plugins
