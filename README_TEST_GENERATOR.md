# Test Automation Code Generator

A flexible tool for generating test automation code across multiple programming languages and testing frameworks.

## Features

- **Multiple Language Support**: Python, JavaScript, TypeScript, Java
- **Multiple Framework Support**: 
  - Python: pytest, unittest
  - JavaScript: Jest, Mocha
  - TypeScript: Jest
  - Java: JUnit 5
- **Structured Test Generation**: Generates well-structured test code with AAA (Arrange-Act-Assert) pattern
- **CLI Interface**: Command-line interface for easy test generation
- **Programmatic API**: Use as a library in your own projects

## Installation

No external dependencies required for basic functionality. For testing:

```bash
pip install pytest
```

## Usage

### Command Line Interface

Generate test code from the command line:

```bash
# Generate Python pytest tests
python test_automation_generator.py \
  --framework pytest \
  --language python \
  --class-name Calculator \
  --methods add subtract multiply divide

# Generate JavaScript Jest tests
python test_automation_generator.py \
  --framework jest \
  --language javascript \
  --class-name UserService \
  --methods createUser deleteUser updateUser

# Generate Java JUnit tests
python test_automation_generator.py \
  --framework junit \
  --language java \
  --class-name DataProcessor \
  --methods processData validateData

# Save output to file
python test_automation_generator.py \
  --framework pytest \
  --language python \
  --class-name Calculator \
  --methods add subtract \
  --output test_calculator.py
```

### Programmatic Usage

Use the generator in your Python code:

```python
from test_automation_generator import TestGenerator, TestFramework, Language

# Create a generator instance
generator = TestGenerator(TestFramework.PYTEST, Language.PYTHON)

# Generate a single test class
test_code = generator.generate_test_class("Calculator", ["add", "subtract", "multiply"])
print(test_code)

# Generate multiple test files
test_specs = [
    {"class_name": "Calculator", "methods": ["add", "subtract"]},
    {"class_name": "StringUtils", "methods": ["concat", "split"]},
]
test_files = generator.generate_test_suite(test_specs)

for filename, code in test_files.items():
    with open(filename, 'w') as f:
        f.write(code)
    print(f"Generated: {filename}")
```

## Supported Combinations

| Language    | Framework | Status |
|-------------|-----------|--------|
| Python      | pytest    | ✅     |
| Python      | unittest  | ✅     |
| JavaScript  | Jest      | ✅     |
| JavaScript  | Mocha     | ✅     |
| TypeScript  | Jest      | ✅     |
| Java        | JUnit     | ✅     |

## Example Output

### Python (pytest)

```python
"""Test suite for Calculator"""

import pytest


class TestCalculator:
    """Test class for Calculator"""

    def test_add(self):
        """Test add functionality"""
        # Arrange
        # Act
        # Assert
        assert True, "Test not implemented"

    def test_subtract(self):
        """Test subtract functionality"""
        # Arrange
        # Act
        # Assert
        assert True, "Test not implemented"
```

### JavaScript (Jest)

```javascript
// Test suite for Calculator

describe('Calculator', () => {
  test('should add', () => {
    // Arrange
    // Act
    // Assert
    expect(true).toBe(true);
  });

  test('should subtract', () => {
    // Arrange
    // Act
    // Assert
    expect(true).toBe(true);
  });
});
```

### Java (JUnit)

```java
// Test suite for Calculator

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    @BeforeEach
    public void setUp() {
        // Set up test fixtures
    }

    @AfterEach
    public void tearDown() {
        // Clean up after tests
    }

    @Test
    public void testAdd() {
        // Test add functionality
        // Arrange
        // Act
        // Assert
        assertTrue(true, "Test not implemented");
    }

    @Test
    public void testSubtract() {
        // Test subtract functionality
        // Arrange
        // Act
        // Assert
        assertTrue(true, "Test not implemented");
    }
}
```

## Running Tests

Run the unit tests for the generator:

```bash
pytest test_test_automation_generator.py -v
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.
