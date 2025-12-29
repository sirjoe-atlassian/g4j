# Test Automation Code Generator

A flexible Python tool for generating automated test code across multiple testing frameworks.

## Features

- **Multi-Framework Support**: Generate tests for:
  - pytest (Python)
  - unittest (Python)
  - Jest (JavaScript)
  - JUnit (Java)

- **Multiple Test Types**:
  - Unit tests
  - Integration tests
  - End-to-End (E2E) tests
  - API tests

- **Customizable Options**:
  - Test fixtures/setup/teardown
  - Mock imports and usage
  - Parametrized tests
  - API-specific test patterns

## Installation

No external dependencies required for the core generator. To run the generated tests, you'll need the respective testing frameworks installed:

```bash
# For pytest
pip install pytest

# For unittest (built-in to Python)
# No installation needed

# For Jest
npm install --save-dev jest

# For JUnit
# Add JUnit dependency to your Maven/Gradle project
```

## Usage

### Basic Usage

```python
from test_automation_generator import generate_test_file, TestFramework, TestType

# Generate a pytest test file
code = generate_test_file(
    framework="pytest",
    test_type="unit",
    test_name="my_function",
    module_path="myapp.mymodule",
    output_path="tests/test_my_function.py",
    include_fixtures=True,
    include_mocks=True,
    include_parametrize=True
)
```

### Advanced Usage with TestConfig

```python
from test_automation_generator import (
    TestCodeGenerator,
    TestConfig,
    TestFramework,
    TestType
)

# Create configuration
config = TestConfig(
    framework=TestFramework.PYTEST,
    test_type=TestType.API,
    test_name="user_endpoint",
    module_path="myapi.users",
    include_fixtures=True,
    include_mocks=True,
    include_parametrize=False
)

# Generate test code
generator = TestCodeGenerator(config)
code = generator.generate()

# Save to file
generator.save_to_file("tests/test_user_endpoint.py")
```

### Command Line Usage

```bash
# Run the generator with example
python test_automation_generator.py
```

## Examples

### Generated pytest Test

```python
"""
Test module for mymodule.myfile
Test Type: unit
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from mymodule.myfile import *


@pytest.fixture
def sample_fixture():
    """Fixture for test setup"""
    # Setup code here
    data = {'key': 'value'}
    yield data
    # Teardown code here


def test_example_function(sample_fixture):
    """Test example_function"""
    # Arrange
    expected = None
    
    # Act
    result = None
    
    # Assert
    assert result == expected
```

### Generated unittest Test

```python
"""
Test module for mymodule
Test Type: unit
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from mymodule import *


class TestMyFunction(unittest.TestCase):
    """Test cases for my_function"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {'key': 'value'}
    
    def tearDown(self):
        """Tear down test fixtures"""
        pass
    
    def test_my_function(self):
        """Test my_function"""
        # Arrange
        expected = None
        
        # Act
        result = None
        
        # Assert
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
```

## Configuration Options

### TestFramework Options
- `PYTEST`: Python pytest framework
- `UNITTEST`: Python unittest framework
- `JEST`: JavaScript Jest framework
- `JUNIT`: Java JUnit framework

### TestType Options
- `UNIT`: Unit tests
- `INTEGRATION`: Integration tests
- `E2E`: End-to-end tests
- `API`: API tests (includes API-specific patterns)

### TestConfig Parameters
- `framework`: Testing framework to use
- `test_type`: Type of test to generate
- `test_name`: Name of the test (will be used in test function names)
- `module_path`: Import path of the module being tested
- `include_fixtures`: Include fixture setup/teardown (default: True)
- `include_mocks`: Include mock imports and examples (default: True)
- `include_parametrize`: Include parametrized test examples (default: False)

## Testing

Run the test suite:

```bash
pytest test_test_automation_generator.py -v
```

## License

MIT License - See licence.md for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Future Enhancements

- Support for more testing frameworks (RSpec, Mocha, etc.)
- Custom template support
- Test generation from function signatures
- Integration with CI/CD pipelines
- Web UI for test generation
