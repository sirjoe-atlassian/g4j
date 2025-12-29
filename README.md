# g4j

## Test Automation Code Generator

This project includes a powerful test automation code generator that can automatically generate test code for:
- Python functions
- Python classes and methods
- API endpoints

See [README_TEST_AUTOMATION.md](README_TEST_AUTOMATION.md) for detailed documentation.

### Quick Start

```python
from test_automation import TestCodeGenerator

# Create generator
generator = TestCodeGenerator(test_framework="pytest")

# Generate function tests
test_cases = [
    {'inputs': {'a': 1, 'b': 2}, 'expected': 3},
]
test_code = generator.generate_function_test(your_function, test_cases)
```

### Features
- ✅ Supports pytest and unittest frameworks
- ✅ Function and class test generation
- ✅ API endpoint test generation
- ✅ Easy-to-use API
- ✅ Export tests to file

## License

This project is licensed under the MIT License - see [licence.md](licence.md) for details.

---

* GT-1 change