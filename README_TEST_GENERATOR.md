# Test Automation Code Generator

A versatile command-line tool for generating test automation code templates for multiple testing frameworks.

## Features

- **Multiple Framework Support**: Generate tests for pytest, unittest, Jest, and JUnit
- **Customizable Templates**: Specify class names and methods to test
- **File Generation**: Output directly to files or stdout
- **AAA Pattern**: All templates follow Arrange-Act-Assert pattern

## Supported Frameworks

- **pytest** - Python's most popular testing framework
- **unittest** - Python's built-in testing framework
- **jest** - JavaScript/TypeScript testing framework
- **junit** - Java's standard testing framework (JUnit 5)

## Installation

No installation required! Just ensure you have Python 3.6+ installed:

```bash
python3 test_generator.py --help
```

## Usage

### Basic Usage

Generate a test template and print to stdout:

```bash
python test_generator.py --framework pytest --name user_service
```

### Generate Tests for Specific Methods

```bash
python test_generator.py \
  --framework pytest \
  --name user_service \
  --class UserService \
  --methods create,update,delete,get
```

### Save to File

```bash
python test_generator.py \
  --framework junit \
  --name calculator \
  --class Calculator \
  --output tests/
```

### More Examples

#### pytest Example
```bash
python test_generator.py -f pytest -n api_client -c ApiClient -m connect,disconnect,send
```

Output: `test_api_client.py`

#### unittest Example
```bash
python test_generator.py -f unittest -n database -c Database -m insert,select,update
```

Output: `test_database.py`

#### Jest Example
```bash
python test_generator.py -f jest -n auth_service -c AuthService -m login,logout,refresh
```

Output: `auth_service.test.js`

#### JUnit Example
```bash
python test_generator.py -f junit -n string_utils -c StringUtils -m reverse,capitalize
```

Output: `TestStringUtils.java`

## Command-Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--framework` | `-f` | Testing framework (pytest, unittest, jest, junit) - **Required** |
| `--name` | `-n` | Name of the test file/class - **Required** |
| `--class` | `-c` | Name of the class being tested - *Optional* |
| `--methods` | `-m` | Comma-separated list of methods to test - *Optional* |
| `--output` | `-o` | Output directory for generated file - *Optional* |

## Generated Template Structure

All generated templates include:

- **Setup/Teardown**: Fixture setup and cleanup methods
- **Test Methods**: Structured test methods following AAA pattern
- **Comments**: Helpful comments for Arrange, Act, Assert sections
- **Framework-specific imports**: Correct imports for each framework

## Example Output

### pytest Template

```python
"""
Test module for UserService
"""

import pytest


class TestUserService:
    """Test class for UserService."""
    
    @pytest.fixture
    def setup(self):
        """Set up test fixtures."""
        # Setup code here
        yield
        # Teardown code here
    
    def test_create(self, setup):
        """Test create method."""
        # Arrange
        
        # Act
        
        # Assert
        assert True, "Test not implemented"
```

### Jest Template

```javascript
/**
 * Test suite for AuthService
 */

describe('AuthService', () => {
    beforeEach(() => {
        // Setup code here
    });
    
    afterEach(() => {
        // Teardown code here
    });
    
    test('login should work correctly', () => {
        // Arrange
        
        // Act
        
        // Assert
        expect(true).toBe(true); // Test not implemented
    });
});
```

## Use Cases

- **Rapid Test Development**: Quickly scaffold test files for new features
- **Team Standardization**: Ensure consistent test structure across the team
- **CI/CD Integration**: Generate test templates as part of build processes
- **Learning Tool**: Help developers learn testing best practices

## Contributing

Feel free to extend the generator with additional frameworks or customization options.

## License

This project is licensed under the MIT License - see the licence.md file for details.
