# g4j

* GT-1 change

hello

## Test Automation Code Generator (DEV-4)

A flexible tool for generating test automation code across multiple programming languages and testing frameworks has been added to this project.

See [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md) for detailed documentation.

### Quick Start

```bash
# Generate Python pytest tests
python test_automation_generator.py \
  --framework pytest \
  --language python \
  --class-name Calculator \
  --methods add subtract multiply divide

# Run examples
python examples.py

# Run unit tests
pytest test_test_automation_generator.py -v
```

### Features
- Supports Python (pytest, unittest), JavaScript (Jest, Mocha), TypeScript (Jest), and Java (JUnit)
- CLI and programmatic API
- Structured test generation with AAA pattern
- Comprehensive test coverage