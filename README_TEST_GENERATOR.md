# Test Automation Code Generator

A Python-based tool to automatically generate test automation code for various testing frameworks.

## Overview

This tool helps developers quickly scaffold test files for different testing frameworks, reducing boilerplate code and accelerating test development.

## Supported Frameworks

- **Python unittest** - Python's built-in testing framework
- **Python pytest** - Popular Python testing framework
- **JavaScript Jest** - JavaScript testing framework
- **Java JUnit** - Java testing framework

## Installation

No installation required. The tool is a standalone Python script that requires Python 3.6+.

## Usage

### List Available Frameworks

```bash
python3 test_automation_generator.py --list-frameworks
```

### Generate Tests

#### Generate to stdout

```bash
python3 test_automation_generator.py --framework python-pytest --name my_test
```

#### Generate to file

```bash
python3 test_automation_generator.py --framework python-unittest --name my_test --output tests/test_my_test.py
```

### Examples

**Python unittest:**
```bash
python3 test_automation_generator.py -f python-unittest -n user_service -o tests/test_user_service.py
```

**Python pytest:**
```bash
python3 test_automation_generator.py -f python-pytest -n api_client -o tests/test_api_client.py
```

**JavaScript Jest:**
```bash
python3 test_automation_generator.py -f javascript-jest -n component_test -o __tests__/component.test.js
```

**Java JUnit:**
```bash
python3 test_automation_generator.py -f java-junit -n calculator -o src/test/java/CalculatorTest.java
```

## Command Line Options

- `--framework`, `-f`: Testing framework to use (required unless listing frameworks)
- `--name`, `-n`: Name of the test (required unless listing frameworks)
- `--output`, `-o`: Output file path (optional, prints to stdout if not specified)
- `--list-frameworks`, `-l`: List available testing frameworks

## Features

- **Multiple Framework Support**: Generate tests for Python, JavaScript, and Java
- **Automatic Naming**: Converts test names to proper class names automatically
- **Timestamped**: Generated files include generation timestamp
- **Extensible**: Easy to add new framework generators
- **CLI & Library**: Can be used as a command-line tool or imported as a Python module

## Using as a Python Library

```python
from test_automation_generator import TestAutomationGenerator

# Generate test code
code = TestAutomationGenerator.generate_test(
    framework='python-pytest',
    test_name='my_feature',
    output_file='tests/test_my_feature.py'
)

# List available frameworks
frameworks = TestAutomationGenerator.list_frameworks()
print(frameworks)
```

## Generated Test Structure

Each generated test includes:
- Test class with proper naming conventions
- Setup and teardown methods/fixtures
- Example test cases
- Framework-specific best practices
- Proper imports and documentation

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

To add a new framework generator:

1. Create a new class inheriting from `TestGenerator`
2. Implement the `generate()` method
3. Add the class to `TestAutomationGenerator.FRAMEWORKS` dictionary
4. Test the new generator

Example:
```python
class MyFrameworkGenerator(TestGenerator):
    def generate(self) -> str:
        return f'''
        # Your template code here
        '''
```

## Future Enhancements

- Support for more testing frameworks (Mocha, TestNG, etc.)
- Custom templates support
- Configuration file support
- Interactive mode for generating tests
- Test case generation from existing code analysis
