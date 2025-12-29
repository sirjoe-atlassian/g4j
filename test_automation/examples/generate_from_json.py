#!/usr/bin/env python3
"""
Example: Generate tests from JSON specification file

This example demonstrates how to generate test suites from a JSON file
containing test specifications.
"""

import sys
import os

# Add parent directory to path to import test_generator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_generator import TestGenerator, load_test_specs_from_json, UNIT_TEST_TEMPLATE


def main():
    """Generate test suite from JSON specifications."""
    # Initialize generator
    generator = TestGenerator(output_dir="generated_tests")
    
    # Register the unit test template
    generator.register_template("unit_test", UNIT_TEST_TEMPLATE)
    
    # Load test specs from JSON file
    json_file = os.path.join(os.path.dirname(__file__), "test_specs.json")
    test_specs = load_test_specs_from_json(json_file)
    
    print(f"Loaded {len(test_specs)} test specifications from {json_file}")
    
    # Generate test suite
    suite_code = generator.generate_test_suite(
        "unit_test",
        test_specs,
        "Auto-Generated Test Suite from JSON"
    )
    
    # Save to file
    output_file = generator.save_test_suite(suite_code, "test_generated_from_json.py")
    
    print(f"\n✓ Successfully generated test suite!")
    print(f"  Output: {output_file}")
    print(f"  Tests: {len(test_specs)}")


if __name__ == "__main__":
    main()
