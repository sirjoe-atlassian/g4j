# Test Automation Code Generator

A flexible and powerful tool to automatically generate test automation code for multiple testing frameworks.

## Features

- **Multi-Framework Support**: Generate test code for:
  - pytest (Python)
  - unittest (Python)
  - Jest (JavaScript)
  - JUnit (Java)
- **Automatic Test Structure**: Generates proper test class structure, setup/teardown methods, and test methods
- **Easy to Use**: Simple command-line interface
- **Extensible**: Easy to add support for more frameworks

## Installation

No additional dependencies required for basic usage. The tool uses Python 3 standard library.

For running generated tests, you'll need the respective testing framework installed:

```bash
# For pytest
pip install pytest

# For unittest (comes with Python)
# No installation needed

# For Jest
npm install --save-dev jest

# For JUnit
# Add JUnit 5 dependency to your Java project
```

## Usage

### Basic Syntax

```bash
python test_generator.py -f <framework> -c <ClassName> -m <method1> <method2> ... [-o output_file]
```

### Parameters

- `-f, --framework`: Test framework to use (required)
  - Choices: `pytest`, `unittest`, `jest`, `junit`
- `-c, --class-name`: Name of the class/module to test (required)
- `-m, --methods`: List of methods to generate tests for (required)
- `-o, --output`: Output file path (optional, prints to stdout if not provided)

### Examples

#### Generate pytest tests

```bash
python test_generator.py -f pytest -c Calculator -m add subtract multiply divide -o test_calculator.py
```

Output: `test_calculator.py`
```python
import pytest
from calculator import Calculator

class TestCalculator:
    """Test suite for Calculator."""
    
    @pytest.fixture
    def instance(self):
        """Create a Calculator instance for testing."""
        return Calculator()
    
    def test_add(self, instance):
        """Test the add method."""
        # TODO: Implement test for add
        result = instance.add()
        assert result is not None, "add should return a value"
    # ... more tests
```

#### Generate unittest tests

```bash
python test_generator.py -f unittest -c UserService -m create_user delete_user update_user -o test_user_service.py
```

#### Generate Jest tests

```bash
python test_generator.py -f jest -c AuthService -m login logout register -o AuthService.test.js
```

#### Generate JUnit tests

```bash
python test_generator.py -f junit -c DataProcessor -m process validate transform -o DataProcessorTest.java
```

#### Print to stdout (no output file)

```bash
python test_generator.py -f pytest -c MyClass -m method1 method2
```

## Generated Test Structure

### pytest
- Test class with descriptive name
- Fixture for test instance setup
- Individual test methods for each method
- Initialization test

### unittest
- Test class inheriting from unittest.TestCase
- setUp and tearDown methods
- Individual test methods
- Initialization test
- Main runner block

### Jest
- describe block for the test suite
- beforeEach and afterEach hooks
- Individual test blocks
- Initialization test

### JUnit
- Test class with proper annotations
- @BeforeEach and @AfterEach methods
- @Test annotated test methods
- Initialization test

## Customization

The generated tests include TODO comments where you need to add specific test logic. Each test method provides a basic structure that you can expand based on your testing needs.

## Example Workflow

1. **Generate the test file**:
   ```bash
   python test_generator.py -f pytest -c Calculator -m add subtract -o test_calculator.py
   ```

2. **Implement the class under test** (if not already done):
   ```python
   # calculator.py
   class Calculator:
       def add(self, a, b):
           return a + b
       
       def subtract(self, a, b):
           return a - b
   ```

3. **Customize the generated tests**:
   ```python
   def test_add(self, instance):
       """Test the add method."""
       result = instance.add(2, 3)
       assert result == 5, "2 + 3 should equal 5"
   ```

4. **Run the tests**:
   ```bash
   pytest test_calculator.py
   ```

## Benefits

- **Save Time**: Quickly scaffold test files without writing boilerplate code
- **Consistency**: All tests follow the same structure and best practices
- **Framework Agnostic**: Support for multiple popular testing frameworks
- **Learning Tool**: Great for developers learning test automation
- **CI/CD Ready**: Generated tests are ready to integrate into your CI/CD pipeline

## Contributing

To add support for a new testing framework:

1. Add the framework to the `TestFramework` enum
2. Implement a `_generate_<framework>` method in the `TestGenerator` class
3. Add the framework to the argument parser choices

## License

See licence.md for details (MIT License).
