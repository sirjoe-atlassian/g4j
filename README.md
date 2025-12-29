# g4j

A test automation code generation toolkit.

## Overview

This project provides utilities for generating test automation code templates across multiple testing frameworks.

## Features

- **Test Code Generator**: Automatically generate test templates for pytest, unittest, Jest, and JUnit
- **Multiple Framework Support**: Works with Python, JavaScript, and Java testing frameworks
- **Customizable Templates**: Specify class names and methods to generate comprehensive test suites
- **CLI Tool**: Easy-to-use command-line interface

## Quick Start

### Generate Test Templates

```bash
# Generate pytest tests
python3 test_generator.py -f pytest -n user_service -c UserService -m create,update,delete

# Generate Jest tests
python3 test_generator.py -f jest -n api_client -m get,post,put

# Generate JUnit tests
python3 test_generator.py -f junit -n calculator -c Calculator -o tests/

# Generate unittest tests
python3 test_generator.py -f unittest -n database -c Database -m connect,disconnect
```

## Documentation

See [README_TEST_GENERATOR.md](README_TEST_GENERATOR.md) for detailed documentation on the test generator tool.

## License

This project is licensed under the MIT License - see the [licence.md](licence.md) file for details.

---

* GT-1 change