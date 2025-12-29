# Test Automation for g4j

This directory contains the test automation framework and test cases for the g4j project.

## Structure

- `__init__.py` - Package initialization
- `conftest.py` - Pytest configuration and shared fixtures
- `test_example.py` - Unittest-based test examples
- `test_pytest_example.py` - Pytest-based test examples

## Running Tests

### Using unittest

```bash
python -m unittest discover tests
```

Or run a specific test file:

```bash
python tests/test_example.py
```

### Using pytest

```bash
pytest tests/
```

Run with verbose output:

```bash
pytest -v tests/
```

Run a specific test file:

```bash
pytest tests/test_pytest_example.py
```

Run a specific test:

```bash
pytest tests/test_pytest_example.py::test_basic_assertion
```

## Test Coverage

To run tests with coverage:

```bash
pytest --cov=. tests/
```

## Writing Tests

### Unittest Style

```python
import unittest

class TestMyFeature(unittest.TestCase):
    def test_something(self):
        self.assertEqual(result, expected)
```

### Pytest Style

```python
def test_my_feature():
    assert result == expected
```

## Fixtures

Common fixtures are defined in `conftest.py` and are available to all tests:

- `sample_data` - Provides sample dictionary data
- `sample_list` - Provides a sample list
- `test_config` - Provides test configuration (session-scoped)

## Best Practices

1. Name test files with `test_` prefix
2. Name test functions with `test_` prefix
3. Use descriptive test names
4. Keep tests independent and isolated
5. Use fixtures for common setup
6. Use parameterized tests for multiple inputs
