# Test Automation Code Generator

A Python-based test automation framework that generates test code from templates and specifications.

## Features

- **Template-based test generation**: Define reusable test templates
- **JSON-driven test specs**: Load test specifications from JSON files
- **Multiple test types**: Support for unit tests, API tests, and custom templates
- **Automatic test suite creation**: Generate complete test suites with multiple test cases
- **Easy extensibility**: Add custom templates for your specific needs

## Installation

No external dependencies required for basic usage. The framework uses Python's standard library.

For API testing features, install:
```bash
pip install requests
```

## Quick Start

### Basic Usage

```python
from test_automation import TestGenerator

# Initialize the generator
generator = TestGenerator(output_dir="generated_tests")

# Register a template
template = '''class Test{class_name}(unittest.TestCase):
    def test_{test_name}(self):
        {test_body}'''

generator.register_template("simple", template)

# Generate a test
test_spec = {
    "class_name": "Calculator",
    "test_name": "addition",
    "test_body": "self.assertEqual(2 + 2, 4)"
}

code = generator.generate_test("simple", test_spec)
print(code)
```

### Generate from JSON

Create a JSON file with test specifications:

```json
[
  {
    "class_name": "Calculator",
    "test_name": "addition",
    "test_description": "addition of two numbers",
    "setup_code": "calc = Calculator()",
    "action_code": "result = calc.add(2, 3)",
    "assertion_code": "self.assertEqual(result, 5)"
  }
]
```

Then generate tests:

```python
from test_automation import TestGenerator, load_test_specs_from_json

generator = TestGenerator()
test_specs = load_test_specs_from_json("specs.json")
suite = generator.generate_test_suite("unit_test", test_specs, "My Test Suite")
generator.save_test_suite(suite, "test_output.py")
```

## Examples

Run the included examples:

```bash
# Generate tests from the example JSON file
cd test_automation/examples
python generate_from_json.py

# Run the main test generator example
cd test_automation
python test_generator.py
```

## Available Templates

### Unit Test Template

Follows the Arrange-Act-Assert pattern:

```python
class Test{class_name}(unittest.TestCase):
    def test_{test_name}(self):
        """Test {test_description}"""
        # Arrange
        {setup_code}
        
        # Act
        {action_code}
        
        # Assert
        {assertion_code}
```

**Required parameters:**
- `class_name`: Name of the class being tested
- `test_name`: Name of the test method
- `test_description`: Description of what is being tested
- `setup_code`: Setup/initialization code
- `action_code`: Code that performs the action
- `assertion_code`: Assertion statements

### API Test Template

For REST API testing:

```python
class Test{api_name}API(unittest.TestCase):
    def test_{test_name}(self):
        """Test {test_description}"""
        url = "{endpoint}"
        payload = {payload}
        response = requests.{method}(url, json=payload)
        self.assertEqual(response.status_code, {expected_status})
        {additional_assertions}
```

**Required parameters:**
- `api_name`: Name of the API
- `test_name`: Name of the test
- `test_description`: Description
- `endpoint`: API endpoint URL
- `payload`: Request payload (JSON)
- `method`: HTTP method (get, post, put, delete)
- `expected_status`: Expected HTTP status code
- `additional_assertions`: Additional assertion code

## Custom Templates

Create your own templates:

```python
generator = TestGenerator()

custom_template = '''
@pytest.mark.{marker}
def test_{test_name}():
    """"{description}"""
    {test_body}
'''

generator.register_template("pytest", custom_template)

spec = {
    "marker": "unit",
    "test_name": "my_feature",
    "description": "Tests my feature",
    "test_body": "assert True"
}

code = generator.generate_test("pytest", spec)
```

## Project Structure

```
test_automation/
├── __init__.py           # Package initialization
├── test_generator.py     # Main test generator module
├── README.md            # This file
└── examples/
    ├── test_specs.json      # Example test specifications
    └── generate_from_json.py # Example script
```

## Use Cases

1. **Regression Testing**: Quickly generate regression tests for multiple scenarios
2. **API Testing**: Generate API tests from OpenAPI/Swagger specifications
3. **Data-Driven Testing**: Create tests from CSV/JSON data files
4. **CI/CD Integration**: Automatically generate tests as part of your pipeline
5. **Test Migration**: Convert tests from one framework to another

## Contributing

Feel free to extend this framework by:
- Adding new templates
- Supporting additional test frameworks (pytest, Jest, etc.)
- Adding more sophisticated code generation features
- Improving template engine capabilities

## License

See licence.md in the project root.
