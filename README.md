# g4j - Test Automation Code Generator

A powerful Python-based test automation code generator that automatically creates test cases from JSON specifications.

## Overview

This project provides a flexible framework for generating test automation code for multiple testing frameworks (pytest, unittest). It's designed to streamline the test creation process by allowing developers to define test specifications in JSON format and automatically generate well-structured test code.

## Features

- 🚀 **Multi-Framework Support**: Generate tests for pytest and unittest
- 📝 **JSON Specification**: Define test cases using simple JSON format
- 🎯 **AAA Pattern**: Generated tests follow Arrange-Act-Assert pattern
- 🔧 **CLI Interface**: Easy-to-use command-line tool
- 📦 **Extensible**: Easy to add support for additional frameworks
- ✅ **Well-Tested**: Comprehensive test suite included

## Quick Start

### Using the CLI

```bash
# Generate pytest tests from JSON specification
python generate_tests.py --spec example_spec.json --framework pytest

# Generate unittest tests with verbose output
python generate_tests.py --spec example_spec.json --framework unittest -v

# Preview generated code without saving
python generate_tests.py --spec example_spec.json --framework pytest --dry-run
```

### Using as a Library

```python
from test_generator import TestGenerator

# Create generator
generator = TestGenerator(framework="pytest")

# Define test cases
test_cases = [
    {
        "name": "addition",
        "description": "Test basic addition",
        "inputs": {"a": 2, "b": 3},
        "expected": 5
    }
]

# Generate and save tests
code = generator.generate_test_class("TestMath", test_cases)
generator.save_test_file(code, "test_math.py")
```

## Project Structure

```
g4j/
├── test_generator.py          # Core test generation library
├── generate_tests.py           # CLI interface
├── test_test_generator.py      # Unit tests
├── example_spec.json           # Example test specification
├── README_TEST_GENERATOR.md    # Detailed documentation
├── licence.md                  # MIT License
└── README.md                   # This file
```

## Documentation

For detailed documentation, see [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md)

## Running Tests

```bash
# Run the unit tests
python -m unittest test_test_generator.TestTestGenerator -v

# Run the example
python test_generator.py
```

## License

This project is licensed under the MIT License - see [licence.md](licence.md) for details.

## Related

* GT-1 change
* Jira Issue: [DEV-4 - Test automation generate code](https://jyang4-test.atlassian.net/browse/DEV-4)