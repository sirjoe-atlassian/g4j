# g4j

## Test Automation Code Generator

This project includes a powerful test automation code generator that supports multiple testing frameworks.

### Features

- **Multi-Framework Support**: Generate tests for pytest, unittest, Jest, and JUnit
- **Command-line Interface**: Easy to use CLI tool
- **Automatic Boilerplate**: Generates test structure, setup/teardown, and test methods
- **Extensible Design**: Easy to add support for more frameworks

### Quick Start

Generate test code using the command-line tool:

```bash
python test_generator.py -f pytest -c Calculator -m add subtract multiply divide -o test_calculator.py
```

### Documentation

See [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md) for detailed documentation, examples, and usage instructions.

### Example Files

- `example_calculator.py` - Example class for demonstration
- `test_calculator_pytest.py` - Generated pytest tests (with customizations)
- `test_calculator_unittest.py` - Generated unittest tests (with customizations)

### License

This project is licensed under the MIT License - see [licence.md](licence.md) for details.

---

* GT-1 change