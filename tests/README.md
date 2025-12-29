# Test Automation Framework

This directory contains automated tests for the g4j project.

## Structure

- `__init__.py` - Package initialization
- `test_sample.py` - Sample test cases demonstrating test patterns
- `test_runner.py` - Test runner utility for executing tests

## Running Tests

### Run all tests
```bash
python -m unittest discover tests
```

Or using the test runner:
```bash
python tests/test_runner.py
```

### Run specific test file
```bash
python -m unittest tests.test_sample
```

### Run specific test class
```bash
python -m unittest tests.test_sample.TestSample
```

### Run specific test method
```bash
python -m unittest tests.test_sample.TestSample.test_basic_assertion
```

## Test Structure

Tests follow the standard unittest framework conventions:
- Test classes inherit from `unittest.TestCase`
- Test methods start with `test_`
- Use `setUp()` for test initialization
- Use `tearDown()` for cleanup

## Adding New Tests

1. Create a new file with prefix `test_` (e.g., `test_feature.py`)
2. Import `unittest`
3. Create test classes inheriting from `unittest.TestCase`
4. Write test methods starting with `test_`

## Best Practices

- Keep tests independent and isolated
- Use descriptive test names
- One assertion per test when possible
- Use subtests for parameterized tests
- Clean up resources in `tearDown()`
