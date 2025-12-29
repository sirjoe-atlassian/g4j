# Test Automation Framework - g4j Project

## Overview
This test automation framework was created for **Jira Issue DEV-4: Test automation generate code**. It provides a comprehensive, extensible solution for automated testing with built-in reporting capabilities.

## Features

- ✅ **Comprehensive Test Framework**: Built on Python's unittest framework
- ✅ **Multiple Report Formats**: JSON, HTML, and plain text reports
- ✅ **Test Result Tracking**: Detailed execution metrics and error logging
- ✅ **Easy Extension**: Base classes for creating custom test suites
- ✅ **Console Summary**: Real-time test execution feedback
- ✅ **Zero External Dependencies**: Uses Python standard library

## Quick Start

### Prerequisites
- Python 3.7 or higher

### Running Tests

1. **Basic execution:**
   ```bash
   python test_automation_framework.py
   ```

2. **Using the test runner:**
   ```bash
   python test_runner.py
   ```

3. **With custom output directory:**
   ```bash
   python test_runner.py --output-dir my_results
   ```

4. **Verbose mode:**
   ```bash
   python test_runner.py --verbose
   ```

## Framework Components

### 1. TestResult
Data class that stores individual test execution results including:
- Test name
- Status (PASSED, FAILED, SKIPPED)
- Execution time
- Error messages
- Timestamp

### 2. TestReporter
Handles test result collection and report generation:
- `add_result()`: Add test results
- `generate_report()`: Generate reports in JSON, HTML, or text format
- `print_summary()`: Display console summary

### 3. BaseTestCase
Enhanced unittest.TestCase with:
- Automatic report generation
- Built-in result tracking
- Pretty console output

### 4. SampleTestSuite
Example test suite demonstrating framework usage with various test scenarios.

## Creating Custom Tests

```python
from test_automation_framework import BaseTestCase, TestResult
import time

class MyCustomTests(BaseTestCase):
    def test_my_feature(self):
        start_time = time.time()
        try:
            # Your test logic here
            self.assertEqual(expected, actual)
            
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_my_feature',
                status='PASSED',
                execution_time=execution_time
            )
            self.reporter.add_result(result)
        except Exception as e:
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_my_feature',
                status='FAILED',
                execution_time=execution_time,
                error_message=str(e)
            )
            self.reporter.add_result(result)
            raise
```

## Report Types

### JSON Report
Located at: `test_results/test_report.json`
- Machine-readable format
- Complete test metrics
- Easy integration with CI/CD systems

### HTML Report
Located at: `test_results/test_report.html`
- Human-readable format
- Visual status indicators
- Styled table layout

### Text Report
Located at: `test_results/test_report.txt`
- Plain text format
- Simple and portable
- Good for logs and archives

## Directory Structure

```
g4j/
├── test_automation_framework.py   # Main framework code
├── test_runner.py                 # Test execution script
├── requirements.txt               # Dependencies
├── README_TEST_AUTOMATION.md      # This file
└── test_results/                  # Generated reports (created on run)
    ├── test_report.json
    ├── test_report.html
    └── test_report.txt
```

## Best Practices

1. **Inherit from BaseTestCase**: Always extend BaseTestCase for custom test classes
2. **Track Results**: Use TestResult to log every test execution
3. **Handle Exceptions**: Wrap test logic in try-except blocks
4. **Descriptive Names**: Use clear, descriptive test method names
5. **Independent Tests**: Ensure tests don't depend on each other

## Extending the Framework

### Adding New Report Formats
Extend the `TestReporter` class and add new methods:
```python
def _generate_xml_report(self) -> str:
    # Your XML generation logic
    pass
```

### Custom Assertions
Add helper methods to your test class:
```python
def assertStatusCode(self, response, expected_code):
    self.assertEqual(response.status_code, expected_code,
                    f"Expected status {expected_code}, got {response.status_code}")
```

## Integration with CI/CD

The framework outputs JSON reports that can be easily integrated with CI/CD pipelines:

```bash
# Example: Jenkins/GitLab CI
python test_runner.py --output-dir reports/
# Parse reports/test_report.json for pass/fail status
```

## Troubleshooting

### Tests not running
- Ensure Python 3.7+ is installed: `python --version`
- Check file permissions
- Verify all files are in the same directory

### Reports not generated
- Check write permissions on output directory
- Ensure test_results/ directory can be created
- Verify disk space availability

## Related Jira Issue
- **Issue**: DEV-4
- **Summary**: Test automation generate code
- **Type**: Subtask
- **Parent**: DEV-2 - Task 2

## License
This project is licensed under the MIT License - see the licence.md file for details.

## Support
For issues or questions, please refer to the project repository or Jira issue DEV-4.
