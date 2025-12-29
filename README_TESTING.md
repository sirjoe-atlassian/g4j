# Test Automation Framework

A comprehensive Python-based test automation framework using pytest for unit, integration, and end-to-end testing.

## Features

- **Multi-layer Testing**: Unit, Integration, and E2E tests
- **API Testing**: Built-in API client with logging and configuration
- **Configurable**: YAML-based configuration with environment support
- **Test Data Generation**: Faker integration for generating realistic test data
- **Parallel Execution**: Support for running tests in parallel
- **Rich Reporting**: HTML reports, code coverage, and detailed logging
- **Markers**: Organized test execution with pytest markers (smoke, regression, api, ui, etc.)

## Project Structure

```
.
├── config/
│   └── config.yaml          # Configuration file for different environments
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   ├── e2e/                 # End-to-end tests
│   └── conftest.py          # Pytest fixtures and configuration
├── utils/
│   ├── api_client.py        # HTTP client for API testing
│   ├── config_reader.py     # Configuration reader utility
│   ├── logger.py            # Logging utility
│   └── test_data_factory.py # Test data generation
├── reports/                 # Test reports and logs (generated)
├── requirements.txt         # Python dependencies
├── pytest.ini              # Pytest configuration
├── Makefile                # Make commands for common tasks
├── run_tests.sh            # Shell script to run tests
└── licence.md              # MIT License
```

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   make install
   ```

4. Configure environment (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Running Tests

### Using Make Commands

```bash
# Run all tests
make test

# Run specific test types
make test-unit          # Unit tests only
make test-integration   # Integration tests only
make test-e2e          # End-to-end tests only
make test-smoke        # Smoke tests only
make test-regression   # Regression tests only

# Run tests in parallel
make test-parallel

# Clean generated files
make clean
```

### Using Shell Script

```bash
# Run all tests
./run_tests.sh all

# Run specific test types
./run_tests.sh unit
./run_tests.sh integration
./run_tests.sh e2e
./run_tests.sh smoke
./run_tests.sh regression

# Run tests in parallel
./run_tests.sh all parallel
```

### Using Pytest Directly

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_sample_unit.py

# Run tests with specific marker
pytest -m smoke
pytest -m "unit and smoke"

# Run tests in parallel
pytest -n auto

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html
```

## Test Markers

The framework uses pytest markers to organize and filter tests:

- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.e2e` - End-to-end tests
- `@pytest.mark.api` - API tests
- `@pytest.mark.ui` - UI tests
- `@pytest.mark.slow` - Long-running tests

## Configuration

### Environment Configuration

Edit `config/config.yaml` to configure different environments:

```yaml
test:
  base_url: "https://api.test.example.com"
  timeout: 30

staging:
  base_url: "https://api.staging.example.com"
  timeout: 30

production:
  base_url: "https://api.example.com"
  timeout: 60
```

Set the environment in `.env` file:
```
ENVIRONMENT=test
BASE_URL=https://api.test.example.com
```

## Writing Tests

### Unit Test Example

```python
import pytest

@pytest.mark.unit
@pytest.mark.smoke
def test_example():
    result = 2 + 2
    assert result == 4
```

### API Test Example

```python
import pytest

@pytest.mark.integration
@pytest.mark.api
def test_api_endpoint(api_client):
    response = api_client.get('/api/v1/users')
    assert response.status_code == 200
    assert len(response.json()) > 0
```

### Using Test Data Factory

```python
from utils.test_data_factory import test_data_factory

def test_with_generated_data(api_client):
    user_data = test_data_factory.create_user_data()
    response = api_client.post('/api/v1/users', json=user_data)
    assert response.status_code == 201
```

## Reports

Test reports are generated in the `reports/` directory:

- **HTML Report**: `reports/report.html` - Detailed test execution report
- **Coverage Report**: `htmlcov/index.html` - Code coverage report
- **Logs**: `reports/logs/` - Detailed execution logs

## CI/CD Integration

The framework can be easily integrated with CI/CD pipelines:

### GitHub Actions Example

```yaml
name: Test Automation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: make install
      - name: Run tests
        run: make test
```

## Best Practices

1. **Keep tests independent**: Each test should be able to run independently
2. **Use fixtures**: Leverage pytest fixtures for setup and teardown
3. **Use markers**: Tag tests appropriately for easy filtering
4. **Mock external dependencies**: Use mocking for unit tests
5. **Keep tests fast**: Optimize test execution time
6. **Use meaningful names**: Test names should describe what they test
7. **Add docstrings**: Document what each test does
8. **Clean up**: Remove test data after execution

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you're in the project root directory
2. **Configuration errors**: Check your `.env` file and `config.yaml`
3. **Network errors**: Verify base URLs and network connectivity
4. **Permission errors**: Ensure test scripts have execute permissions

## Contributing

1. Write tests for new features
2. Ensure all tests pass before submitting
3. Follow the existing code structure
4. Update documentation as needed

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.
