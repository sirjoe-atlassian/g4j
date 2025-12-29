# Test Automation Framework

This test automation framework was created for Jira issue **DEV-4: Test automation generate code**.

## Overview

This project provides a comprehensive test automation framework with support for:
- **API Testing**: Helper methods for validating API responses, status codes, and data
- **UI Testing**: Helper methods for validating UI elements and content
- **Test Runner**: Custom test runner with detailed logging and reporting
- **Pytest Integration**: Full compatibility with pytest for advanced testing features

## Project Structure

```
.
├── test_automation.py       # Main test automation framework
├── tests/
│   ├── __init__.py
│   └── test_sample.py      # Sample test cases demonstrating the framework
├── requirements.txt         # Python dependencies
├── licence.md              # MIT License
└── README_TEST_AUTOMATION.md # This file
```

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Built-in Test Runner

Execute the main test automation script:
```bash
python test_automation.py
```

This will run sample tests and display a summary report.

### Running Pytest Tests

Execute all tests with pytest:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_sample.py -v
```

## Framework Components

### TestRunner

A custom test runner that executes tests and tracks results:

```python
from test_automation import TestRunner

runner = TestRunner()

def my_test():
    assert 2 + 2 == 4

runner.run_test("My Test", my_test)
runner.print_summary()
```

### APITestHelper

Helper class for API testing:

```python
from test_automation import APITestHelper

# Assert status code
APITestHelper.assert_status_code(200, 200)

# Assert response contains key
response = {'status': 'success', 'data': {'id': 1}}
APITestHelper.assert_response_contains(response, 'status')

# Assert response value
APITestHelper.assert_response_value(response, 'status', 'success')
```

### UITestHelper

Helper class for UI testing:

```python
from test_automation import UITestHelper

# Assert element is present
UITestHelper.assert_element_present(element)

# Assert element is visible
UITestHelper.assert_element_visible(True)

# Assert text equals expected value
UITestHelper.assert_text_equals(actual_text, "Expected Text")
```

## Writing Tests

### Using Pytest

```python
import pytest
from test_automation import APITestHelper

class TestAPI:
    def test_api_response(self):
        response = {'status': 'ok'}
        APITestHelper.assert_response_contains(response, 'status')
```

### Using Custom TestRunner

```python
from test_automation import TestRunner

runner = TestRunner()

def test_calculation():
    assert 5 + 5 == 10

runner.run_test("Calculation Test", test_calculation)
summary = runner.get_summary()
```

## Features

- ✅ Custom test runner with detailed logging
- ✅ API testing helpers
- ✅ UI testing helpers
- ✅ Pytest integration
- ✅ Test result tracking and reporting
- ✅ Comprehensive error handling
- ✅ Execution time tracking
- ✅ Pass rate calculation

## Test Results

All tests are currently passing:
- Main test automation: 3/3 tests passed (100%)
- Pytest test suite: 15/15 tests passed (100%)

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.
