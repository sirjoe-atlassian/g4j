# Test Automation Code Generator

A Python tool that automatically generates test code scaffolding from source files, supporting both pytest and unittest frameworks.

## Overview

This project implements automated test code generation for Python projects. It analyzes source files using AST (Abstract Syntax Tree) parsing and creates comprehensive test stubs following best practices.

## Features

- **Automatic Test Generation**: Analyzes Python source files and generates test stubs for all functions and methods
- **Multiple Framework Support**: Generates tests for both pytest and unittest frameworks
- **Smart Parsing**: Extracts function signatures, arguments, docstrings, and type annotations
- **Template-Based**: Creates well-structured test templates following AAA (Arrange-Act-Assert) pattern
- **CLI Interface**: Easy-to-use command-line interface

## Quick Start

Generate pytest tests:
```bash
python3 test_generator.py your_module.py
```

Generate unittest tests:
```bash
python3 test_generator.py your_module.py -f unittest -o test_your_module.py
```

## Documentation

For detailed documentation, see [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md)

## Testing

Run the test suite:
```bash
python3 -m pytest test_test_generator.py -v
```

## License

This project is licensed under the MIT License - see [licence.md](licence.md) for details.

## Related

- Jira Issue: [DEV-4 - Test automation generate code](https://jyang4-test.atlassian.net/browse/DEV-4)
- Parent Task: DEV-2 - Task 2