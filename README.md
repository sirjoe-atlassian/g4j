# g4j

A project with test automation framework.

## Overview

This project includes a comprehensive test automation framework with example test cases.

## Features

- Unit testing support with unittest
- Pytest support with fixtures and parameterized tests
- Test coverage reporting
- Well-structured test organization

## Project Structure

```
g4j/
├── README.md           # Project documentation
├── licence.md          # MIT License
├── requirements-test.txt  # Test dependencies
└── tests/              # Test automation framework
    ├── __init__.py
    ├── conftest.py     # Pytest fixtures
    ├── test_example.py # Unittest examples
    ├── test_pytest_example.py  # Pytest examples
    └── README.md       # Test documentation
```

## Getting Started

### Installation

1. Clone the repository
2. Install test dependencies (optional, for pytest):
   ```bash
   pip install -r requirements-test.txt
   ```

### Running Tests

Using unittest (no additional dependencies required):
```bash
python -m unittest discover tests
```

Or run specific test file:
```bash
python tests/test_example.py
```

Using pytest (requires installation):
```bash
pytest tests/
```

## Test Automation

For detailed information about the test automation framework, see [tests/README.md](tests/README.md).

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Changes

* GT-1 change