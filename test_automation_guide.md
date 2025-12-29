# Test Automation Code Generator

## Overview

This test automation code generator helps you automatically generate test code for multiple testing frameworks and programming languages. It supports a specification-driven approach where you can define test cases in JSON format and generate the corresponding test code.

## Supported Frameworks

- **Python**: 
  - pytest
  - unittest
- **Java**:
  - JUnit 5
- **JavaScript**:
  - Jest

## Features

- Generate test suites from JSON specifications
- Support for multiple test frameworks
- Automatic test case generation with setup, assertions, and teardown
- Extensible architecture for adding new frameworks
- Type-safe test case definitions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Define Test Specifications in JSON

Create a JSON file with your test specifications (see `test_spec_example.json`):

```json
{
  "class_name": "CalculatorTests",
  "test_cases": [
    {
      "name": "addition",
      "description": "Test addition operation",
      "setup": "calculator = Calculator()",
      "assertions": [
        "result = calculator.add(2, 3)",
        "assert result == 5"
      ]
    }
  ]
}
```

### 2. Generate Test Code

#### Using Python API

```python
from test_generator import TestFramework, generate_from_json

# Generate pytest tests
generate_from_json(
    json_file='test_spec_example.json',
    framework=TestFramework.PYTEST,
    output_file='test_calculator.py'
)
```

#### Using Command Line

```bash
python test_generator.py
```

### 3. Programmatic Usage

```python
from test_generator import (
    TestCase, 
    TestFramework, 
    create_generator
)

# Create test cases
test_cases = [
    TestCase(
        name="addition",
        description="Test addition operation",
        setup="calculator = Calculator()",
        assertions=[
            "result = calculator.add(2, 3)",
            "assert result == 5"
        ]
    )
]

# Generate code
generator = create_generator(TestFramework.PYTEST)
code = generator.generate_test_suite(test_cases, "CalculatorTests")
print(code)
```

## JSON Specification Format

### Test Suite Structure

```json
{
  "class_name": "TestSuiteName",
  "test_cases": [...]
}
```

### Test Case Structure

```json
{
  "name": "test_name",
  "description": "What the test does",
  "setup": "Setup code (optional)",
  "teardown": "Teardown code (optional)",
  "assertions": [
    "assertion 1",
    "assertion 2"
  ],
  "test_data": {
    "key": "value"
  }
}
```

## Examples

### Pytest Example

Generated output:
```python
import pytest

class CalculatorTests:
    """Generated test suite"""

    def test_addition(self):
        """Test addition operation"""
        # Setup
        calculator = Calculator()

        # Test execution
        result = calculator.add(2, 3)
        assert result == 5
```

### JUnit Example

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTests {

    @Test
    public void testAddition() {
        // Test addition operation
        // Setup
        Calculator calculator = new Calculator();

        // Test execution
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }
}
```

### Jest Example

```javascript
describe('CalculatorTests', () => {

  test('addition', () => {
    // Test addition operation
    // Setup
    const calculator = new Calculator();

    // Test execution
    const result = calculator.add(2, 3);
    expect(result).toBe(5);
  });
});
```

## Extending the Generator

To add support for a new framework:

1. Create a new generator class that extends `TestGenerator`
2. Implement `generate_test_suite()` and `generate_test_case()` methods
3. Add the new framework to the `TestFramework` enum
4. Register it in the `create_generator()` factory function

Example:

```python
class MyFrameworkGenerator(TestGenerator):
    def __init__(self):
        super().__init__(TestFramework.MY_FRAMEWORK, Language.PYTHON)
    
    def generate_test_suite(self, test_cases, class_name):
        # Implementation
        pass
    
    def generate_test_case(self, test_case):
        # Implementation
        pass
```

## Best Practices

1. **Keep test cases focused**: Each test should verify one specific behavior
2. **Use descriptive names**: Test names should clearly indicate what is being tested
3. **Include proper setup/teardown**: Clean up resources after tests
4. **Document test intent**: Use the description field to explain what the test verifies
5. **Organize test data**: Use the test_data field for test-specific configuration

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)
2. **JSON parsing errors**: Validate your JSON specification file
3. **Framework not supported**: Check if your framework is in the supported list

## License

This project is licensed under the MIT License - see the licence.md file for details.
