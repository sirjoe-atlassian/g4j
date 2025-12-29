# g4j

A project with automated test generation capabilities.

* GT-1 change

## Features

- Test automation framework
- Sample test cases and patterns
- Test runner utilities

## Project Structure

```
g4j/
├── README.md           # Project documentation
├── licence.md          # MIT License
└── tests/              # Test automation framework
    ├── __init__.py     # Package initialization
    ├── README.md       # Test documentation
    ├── test_sample.py  # Sample test cases
    └── test_runner.py  # Test execution utility
```

## Getting Started

### Running Tests

Run all tests:
```bash
python tests/test_runner.py
```

Or use unittest discovery:
```bash
python -m unittest discover tests
```

### License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.