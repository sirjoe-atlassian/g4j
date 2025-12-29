# g4j

* GT-1 change

## Test Automation Code Generator (DEV-4)

This repository includes a powerful test automation code generator that can create test files for multiple testing frameworks.

### Features
- Multi-framework support: pytest, unittest, Jest, JUnit
- Multiple test types: Unit, Integration, E2E, API
- Customizable templates with fixtures, mocks, and parametrized tests

### Quick Start

```python
from test_automation_generator import generate_test_file

# Generate a test file
generate_test_file(
    framework="pytest",
    test_type="unit",
    test_name="my_function",
    module_path="mymodule",
    output_path="tests/test_my_function.py"
)
```

### Documentation
See [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md) for detailed documentation.

### Examples
Run `python example_usage.py` to see various usage examples.

### License
This project is licensed under the MIT License - see [licence.md](licence.md) for details.