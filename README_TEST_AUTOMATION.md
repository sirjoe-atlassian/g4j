# Test Automation Framework

**Jira Issue:** DEV-4 - Test automation generate code

## Overview

This test automation framework provides a comprehensive solution for automated testing. It includes:

- **Test Framework Core** (`test_automation.py`) - Main framework with test execution and reporting
- **Configuration** (`test_config.json`) - Centralized configuration for test settings
- **Dependencies** (`requirements.txt`) - Required Python packages

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests

```bash
python test_automation.py
```

### 3. View Results

Test results will be displayed in the console and a detailed report will be generated as `test_report.txt`.

## Framework Features

### Core Components

- **TestAutomationFramework**: Main framework class
  - Configurable logging
  - Test suite execution
  - Result tracking and reporting
  
- **Sample Test Cases**: 
  - `SampleTestCase`: Basic unit test examples
  - `APITestCase`: API testing examples

### Configuration

Edit `test_config.json` to customize:
- Log levels
- Retry settings
- Timeout values
- Environment configurations
- Test suite selection

### Logging

The framework includes comprehensive logging:
- Console output with timestamps
- Configurable log levels (DEBUG, INFO, WARNING, ERROR)
- Test execution tracking

### Reporting

Automatic generation of test reports including:
- Total tests executed
- Pass/fail counts
- Execution duration
- Error details

## Extending the Framework

### Adding New Test Cases

```python
import unittest

class MyNewTestCase(unittest.TestCase):
    def setUp(self):
        # Setup code here
        pass
    
    def test_my_feature(self):
        # Your test code
        self.assertTrue(True)
    
    def tearDown(self):
        # Cleanup code here
        pass
```

### Running Custom Test Suites

```python
from test_automation import TestAutomationFramework, MyNewTestCase

framework = TestAutomationFramework()
results = framework.run_test_suite([MyNewTestCase])
framework.generate_report()
```

## Best Practices

1. **Keep tests independent**: Each test should be able to run independently
2. **Use descriptive names**: Test method names should clearly describe what they test
3. **Setup and teardown**: Use setUp() and tearDown() for test initialization and cleanup
4. **Assertions**: Use appropriate assertion methods for better error messages
5. **Documentation**: Add docstrings to test methods explaining what they verify

## Available Test Types

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **API Tests**: Test API endpoints and responses
- **End-to-End Tests**: Test complete user workflows

## CI/CD Integration

This framework can be integrated with CI/CD pipelines:

```bash
# Example CI command
python test_automation.py && echo "Tests passed" || exit 1
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`
2. **Test Failures**: Check test logs for detailed error messages
3. **Configuration Issues**: Verify `test_config.json` syntax is valid JSON

## License

See `licence.md` for license information (MIT License).

## Support

For issues related to this test automation framework, please refer to the parent task DEV-2 or contact the development team.
