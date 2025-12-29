"""
Test Automation Framework

A simple framework for generating automated test code from templates and specifications.
"""

from .test_generator import TestGenerator, load_test_specs_from_json

__version__ = "1.0.0"
__all__ = ["TestGenerator", "load_test_specs_from_json"]
