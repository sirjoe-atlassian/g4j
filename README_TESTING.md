# Test Automation Framework

A comprehensive test automation framework built with Python and pytest, supporting API, web UI, and unit testing.

## Features

- **API Testing**: HTTP client with support for REST APIs
- **Web UI Testing**: Selenium-based browser automation
- **Unit Testing**: Framework for component testing
- **Configuration Management**: Environment-based configuration
- **Logging**: Comprehensive logging for debugging
- **Parallel Execution**: Run tests in parallel for faster execution
- **Multiple Browsers**: Support for Chrome and Firefox
- **Reporting**: HTML and Allure report generation
- **Test Data Management**: JSON-based test data handling

## Project Structure

```
.
├── src/
│   ├── config/
│   │   └── config.py          # Configuration management
│   └── utils/
│       ├── api_client.py      # API testing utilities
│       ├── logger.py          # Logging utilities
│       └── test_data.py       # Test data management
├── tests/
│   ├── api/                   # API tests
│   ├── integration/           # Integration/Web UI tests
│   └── unit/                  # Unit tests
├── conftest.py                # Pytest fixtures and configuration
├── pytest.ini                 # Pytest settings
├── requirements.txt           # Python dependencies
├── run_tests.sh              # Test execution script (Linux/Mac)
├── run_tests.bat             # Test execution script (Windows)
└── licence.md                # MIT License

```

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chrome or Firefox browser (for web tests)

### Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
   - **Linux/Mac**: `source venv/bin/activate`
   - **Windows**: `venv\Scripts\activate.bat`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install browser drivers (if running web tests):
   - Chrome: Download [ChromeDriver](https://chromedriver.chromium.org/)
   - Firefox: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

## Running Tests

### Using Scripts

**Linux/Mac:**
```bash
chmod +x run_tests.sh
./run_tests.sh                    # Run all tests
./run_tests.sh --unit             # Run unit tests only
./run_tests.sh --integration      # Run integration tests only
./run_tests.sh --smoke            # Run smoke tests only
./run_tests.sh --parallel         # Run tests in parallel
```

**Windows:**
```cmd
run_tests.bat                     # Run all tests
run_tests.bat --unit              # Run unit tests only
run_tests.bat --integration       # Run integration tests only
run_tests.bat --smoke             # Run smoke tests only
run_tests.bat --parallel          # Run tests in parallel
```

### Using pytest directly

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_sample_unit.py

# Run tests by marker
pytest -m smoke
pytest -m unit
pytest -m integration
pytest -m regression

# Run tests in parallel
pytest -n auto

# Run with verbose output
pytest -v

# Generate HTML report
pytest --html=reports/report.html

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

## Configuration

Configure the framework using environment variables:

```bash
# API Configuration
export API_BASE_URL="https://api.example.com"
export API_TIMEOUT="30"

# Web Configuration
export WEB_BASE_URL="https://www.example.com"
export BROWSER="chrome"  # or "firefox"
export HEADLESS="false"  # Set to "true" for headless mode
export IMPLICIT_WAIT="10"

# Test Configuration
export PARALLEL_WORKERS="4"
export SCREENSHOT_ON_FAILURE="true"
```

Or create a `.env` file in the project root with the above variables.

## Writing Tests

### API Tests Example

```python
import pytest
from src.utils.api_client import APIClient

@pytest.mark.integration
class TestAPI:
    def test_get_users(self, api_client):
        response = api_client.get('/users')
        assert response.status_code == 200
        assert isinstance(response.json(), list)
```

### Web UI Tests Example

```python
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.integration
class TestWebUI:
    def test_homepage(self, browser):
        browser.get('https://www.example.com')
        assert 'Example' in browser.title
```

### Unit Tests Example

```python
import pytest

@pytest.mark.unit
class TestMath:
    def test_addition(self):
        assert 2 + 2 == 4
```

## Test Markers

- `@pytest.mark.smoke` - Critical functionality tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.integration` - Integration and E2E tests
- `@pytest.mark.unit` - Unit tests

## Reporting

### HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Coverage Report
```bash
pytest --cov=src --cov-report=html
```

### Allure Report
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Best Practices

1. **Use Page Object Model** for web UI tests
2. **Keep tests independent** - each test should be able to run alone
3. **Use fixtures** for setup and teardown
4. **Implement proper waits** instead of hardcoded sleeps
5. **Use meaningful assertions** with descriptive messages
6. **Follow naming conventions** - test files start with `test_`
7. **Organize tests** by functionality or feature
8. **Keep test data separate** from test logic

## Troubleshooting

### Browser Driver Issues
- Ensure browser driver is in PATH or specify driver path
- Check browser and driver version compatibility

### Import Errors
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Test Failures
- Check logs in `logs/` directory
- Review screenshots in `screenshots/` directory (for failed web tests)
- Run tests with `-v` flag for verbose output

## Contributing

1. Create a feature branch
2. Write tests for new functionality
3. Ensure all tests pass
4. Update documentation
5. Submit pull request

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.
