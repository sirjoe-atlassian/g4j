# Test Automation Framework

A comprehensive test automation framework for API and UI testing, developed for Jira issue DEV-4.

## Features

- **Test Runner**: Automated test discovery and execution with detailed reporting
- **API Testing**: Helper classes for REST API testing with common assertions
- **UI Testing**: Selenium-based helper classes for web UI automation
- **Example Tests**: Ready-to-run example test suites demonstrating the framework

## Project Structure

```
.
├── test_automation/
│   ├── __init__.py
│   ├── test_runner.py          # Main test runner with reporting
│   ├── api_test_helper.py      # API testing utilities
│   └── ui_test_helper.py       # UI testing utilities (Selenium)
├── tests/
│   ├── __init__.py
│   ├── test_example.py         # Basic unit test examples
│   └── test_api_example.py     # API test examples
├── requirements.txt            # Python dependencies
└── README_TEST_AUTOMATION.md   # This file
```

## Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. For UI testing, ensure you have the appropriate browser drivers installed:
   - Chrome: [ChromeDriver](https://chromedriver.chromium.org/)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver)
   - Edge: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage

### Running All Tests

Run all tests using the test runner:

```bash
python test_automation/test_runner.py
```

### Running Specific Test Files

Run a specific test file:

```bash
python -m unittest tests/test_example.py
```

Run API tests:

```bash
python -m unittest tests/test_api_example.py
```

### Running Individual Test Classes or Methods

Run a specific test class:

```bash
python -m unittest tests.test_example.TestMathOperations
```

Run a specific test method:

```bash
python -m unittest tests.test_example.TestMathOperations.test_addition
```

## API Testing

### Basic Usage

```python
from test_automation.api_test_helper import APITestHelper

# Initialize API helper
api = APITestHelper(
    base_url='https://api.example.com',
    default_headers={'Authorization': 'Bearer token'}
)

# Make requests
response = api.get('/users')
api.assert_status_code(response, 200)
api.assert_response_contains(response, 'data')
```

### Available API Methods

- `get(endpoint, params, headers)` - GET request
- `post(endpoint, data, json_data, headers)` - POST request
- `put(endpoint, data, json_data, headers)` - PUT request
- `delete(endpoint, headers)` - DELETE request
- `assert_status_code(response, expected_code)` - Assert status code
- `assert_response_contains(response, key)` - Assert response contains key
- `assert_response_value(response, key, expected_value)` - Assert response value

## UI Testing

### Basic Usage

```python
from test_automation.ui_test_helper import UITestHelper
from selenium.webdriver.common.by import By

# Initialize UI helper
ui = UITestHelper(browser='chrome', headless=False)

# Start browser and navigate
ui.start_browser()
ui.navigate_to('https://example.com')

# Interact with elements
ui.click_element('button#submit', by=By.CSS_SELECTOR)
ui.enter_text('input#username', 'testuser')
text = ui.get_text('h1.title')

# Clean up
ui.stop_browser()
```

### Available UI Methods

- `start_browser()` - Start browser instance
- `stop_browser()` - Close browser instance
- `navigate_to(url)` - Navigate to URL
- `find_element(locator, by, timeout)` - Find element with wait
- `click_element(locator, by, timeout)` - Click element
- `enter_text(locator, text, by, timeout, clear_first)` - Enter text
- `get_text(locator, by, timeout)` - Get element text
- `is_element_visible(locator, by, timeout)` - Check element visibility
- `take_screenshot(filename)` - Take screenshot
- `get_current_url()` - Get current URL
- `get_page_title()` - Get page title

## Test Runner Features

The test runner provides:

- Automatic test discovery
- Detailed test execution output
- Test result summary with statistics
- Success rate calculation
- Timestamp for test runs

### Test Report Example

```
======================================================================
Test Summary
======================================================================
Timestamp: 2025-12-29T10:30:00.000000
Total Tests: 15
Failures: 0
Errors: 0
Skipped: 0
Success Rate: 100.00%
======================================================================
```

## Writing Tests

### Unit Test Example

```python
import unittest

class TestExample(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test."""
        self.data = [1, 2, 3]
    
    def tearDown(self):
        """Clean up after each test."""
        pass
    
    def test_something(self):
        """Test description."""
        self.assertEqual(len(self.data), 3)
```

### API Test Example

```python
import unittest
from test_automation.api_test_helper import APITestHelper

class TestAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up once for all tests in class."""
        cls.api = APITestHelper(base_url='https://api.example.com')
    
    def test_get_resource(self):
        """Test GET endpoint."""
        response = self.api.get('/resource/1')
        self.api.assert_status_code(response, 200)
```

## Best Practices

1. **Test Isolation**: Each test should be independent and not rely on other tests
2. **Setup and Teardown**: Use setUp() and tearDown() for test fixtures
3. **Descriptive Names**: Use clear, descriptive test method names
4. **Assertions**: Use appropriate assertions for better error messages
5. **Documentation**: Add docstrings to describe what each test does
6. **Error Handling**: Handle expected errors with assertRaises()

## Extending the Framework

### Adding Custom Helpers

Create custom helper modules in the `test_automation/` directory:

```python
# test_automation/custom_helper.py
class CustomHelper:
    def custom_method(self):
        # Your implementation
        pass
```

### Adding Test Data

Create a `test_data/` directory for test data files:

```
test_data/
├── api_test_data.json
├── ui_test_data.csv
└── fixtures.yaml
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure the project root is in your Python path
2. **Browser Driver Errors**: Verify browser drivers are installed and in PATH
3. **Network Errors**: Check API endpoint availability and credentials
4. **Timeout Errors**: Increase timeout values for slow operations

## Contributing

When adding new tests or features:

1. Follow existing code style and conventions
2. Add appropriate documentation
3. Include example usage
4. Update this README if needed

## License

See LICENSE.md for license information.
