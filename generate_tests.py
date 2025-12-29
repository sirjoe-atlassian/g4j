#!/usr/bin/env python3
"""
Command-line interface for the Test Generator.

Usage:
    python generate_tests.py --spec example_spec.json --framework pytest --output tests/
"""

import argparse
import sys
import json
from pathlib import Path
from test_generator import TestGenerator


def load_spec_from_file(filepath: str) -> dict:
    """Load test specification from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Specification file '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in specification file: {e}")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate test automation code from specifications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate pytest tests from JSON spec
  python generate_tests.py --spec example_spec.json --framework pytest

  # Generate unittest tests with custom output directory
  python generate_tests.py --spec example_spec.json --framework unittest --output custom_tests/

  # Display generated code without saving
  python generate_tests.py --spec example_spec.json --framework pytest --dry-run
        """
    )
    
    parser.add_argument(
        '--spec',
        type=str,
        required=True,
        help='Path to the JSON specification file'
    )
    
    parser.add_argument(
        '--framework',
        type=str,
        choices=['pytest', 'unittest'],
        default='pytest',
        help='Testing framework to use (default: pytest)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='tests',
        help='Output directory for generated tests (default: tests/)'
    )
    
    parser.add_argument(
        '--filename',
        type=str,
        help='Output filename (default: auto-generated from class name)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print generated code without saving to file'
    )
    
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Load specification
    if args.verbose:
        print(f"Loading specification from: {args.spec}")
    
    spec = load_spec_from_file(args.spec)
    
    # Extract specification details
    class_name = spec.get('class_name', 'GeneratedTest')
    test_cases = spec.get('test_cases', [])
    
    if not test_cases:
        print("Warning: No test cases found in specification.")
        sys.exit(1)
    
    if args.verbose:
        print(f"Class name: {class_name}")
        print(f"Number of test cases: {len(test_cases)}")
        print(f"Framework: {args.framework}")
    
    # Generate test code
    generator = TestGenerator(framework=args.framework)
    test_code = generator.generate_test_class(class_name, test_cases)
    
    # Dry run mode - just print the code
    if args.dry_run:
        print("\n" + "=" * 70)
        print("Generated Test Code (Dry Run)")
        print("=" * 70 + "\n")
        print(test_code)
        return
    
    # Determine output filename
    if args.filename:
        output_filename = args.filename
    else:
        # Convert class name to snake_case for filename
        import re
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        output_filename = f"{snake_case}.py"
    
    # Save to file
    try:
        output_path = generator.save_test_file(
            test_code,
            output_filename,
            output_dir=args.output
        )
        
        print(f"✓ Test file successfully generated: {output_path}")
        print(f"  Framework: {args.framework}")
        print(f"  Test cases: {len(test_cases)}")
        
        if args.verbose:
            print("\nGenerated test methods:")
            for i, tc in enumerate(test_cases, 1):
                test_name = tc.get('name', f'case_{i}')
                print(f"  - test_{test_name}")
        
    except Exception as e:
        print(f"Error: Failed to save test file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
