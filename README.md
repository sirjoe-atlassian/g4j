# g4j - Test Automation Code Generator

A flexible Python tool for automatically generating test automation code for various testing frameworks and programming languages.

## Project Overview

This project implements a test automation code generator that helps developers quickly scaffold test files with proper structure and boilerplate code. It supports multiple testing frameworks across different programming languages.

## Features

- **Multi-Framework Support**: pytest, unittest, Jest, JUnit
- **Multi-Language**: Python, JavaScript, Java
- **Automatic Boilerplate**: Generates imports, fixtures/setup methods, and test stubs
- **Arrange-Act-Assert Pattern**: All tests follow the AAA testing pattern
- **CLI Interface**: Easy-to-use command-line tool
- **Programmatic API**: Can be imported and used in Python scripts

## Quick Start

```bash
# Generate pytest tests
python test_generator.py --framework pytest --language python \
  --class-name Calculator --methods add subtract multiply divide \
  --output tests/test_calculator.py

# View help
python test_generator.py --help
```

## Documentation

- [Test Generator Documentation](README_TEST_GENERATOR.md) - Comprehensive usage guide
- [Examples](examples/) - Sample code and generated tests
- [License](licence.md) - MIT License

## Project Structure

```
.
├── README.md                    # This file
├── README_TEST_GENERATOR.md     # Detailed documentation
├── licence.md                   # MIT License
├── test_generator.py            # Main test generator tool
└── examples/                    # Example usage
    ├── README.md                # Examples documentation
    ├── sample_calculator.py     # Sample class
    └── test_calculator.py       # Generated test file
```

## Supported Combinations

| Language   | Frameworks        |
|------------|-------------------|
| Python     | pytest, unittest  |
| JavaScript | Jest              |
| Java       | JUnit             |

## Usage Examples

### Python with pytest
```bash
python test_generator.py --framework pytest --language python \
  --class-name UserService --methods create delete update
```

### JavaScript with Jest
```bash
python test_generator.py --framework jest --language javascript \
  --class-name ShoppingCart --methods addItem removeItem
```

### Java with JUnit
```bash
python test_generator.py --framework junit --language java \
  --class-name OrderProcessor --methods process cancel
```

## Requirements

- Python 3.6+
- No external dependencies for the generator itself
- Target frameworks must be installed separately (pytest, jest, junit, etc.)

## License

This project is licensed under the MIT License. See [licence.md](licence.md) for details.

## Contributing

Contributions are welcome! Future enhancements may include additional frameworks, languages, and features like mock generation.

---

* GT-1 change