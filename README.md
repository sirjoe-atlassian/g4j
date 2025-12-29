# Test Automation Code Generator (g4j)

A powerful and flexible test automation code generator that supports multiple testing frameworks and programming languages.

## Features

- 🚀 Generate test code for multiple frameworks (pytest, unittest, JUnit, Jest)
- 📝 JSON-based test specification
- 🔧 Programmatic API for dynamic test generation
- 🎯 Support for setup, teardown, and assertions
- 📦 Extensible architecture for adding new frameworks

## Supported Frameworks

- **Python**: pytest, unittest
- **Java**: JUnit 5
- **JavaScript**: Jest

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from test_generator import TestCase, TestFramework, create_generator

# Create test cases
test_cases = [
    TestCase(
        name="addition",
        description="Test addition operation",
        setup="calculator = Calculator()",
        assertions=["result = calculator.add(2, 3)", "assert result == 5"]
    )
]

# Generate code
generator = create_generator(TestFramework.PYTEST)
code = generator.generate_test_suite(test_cases, "CalculatorTests")
print(code)
```

### Generate from JSON

```bash
python test_generator.py
```

Or use the API:

```python
from test_generator import TestFramework, generate_from_json

generate_from_json(
    json_file='test_spec_example.json',
    framework=TestFramework.PYTEST,
    output_file='test_calculator.py'
)
```

## Documentation

See [test_automation_guide.md](test_automation_guide.md) for comprehensive documentation.

## Project Structure

```
.
├── README.md                    # This file
├── licence.md                   # MIT License
├── test_generator.py            # Main generator module
├── test_test_generator.py       # Unit tests
├── test_spec_example.json       # Example JSON specification
├── test_automation_guide.md     # Detailed documentation
└── requirements.txt             # Python dependencies
```

## Running Tests

```bash
pytest test_test_generator.py -v
```

All 22 tests pass successfully! ✅

## Example Output

### Pytest

```python
import pytest

class CalculatorTests:
    """Generated test suite"""

    def test_addition(self):
        """Test addition operation"""
        # Setup
        calculator = Calculator()

        # Test execution
        result = calculator.add(2, 3)
        assert result == 5
```

### JUnit

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTests {

    @Test
    public void testAddition() {
        // Test addition operation
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }
}
```

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

## Contributing

Contributions are welcome! Feel free to:

1. Add support for new testing frameworks
2. Enhance existing generators
3. Improve documentation
4. Report bugs or suggest features

## Related

* Jira Issue: DEV-4 - Test automation generate code