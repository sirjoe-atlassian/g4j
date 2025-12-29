"""
Test Runner Script
Runs the test automation framework and generates reports
"""

import sys
import os
import argparse
from test_automation_framework import run_tests


def main():
    """Main entry point for test runner"""
    parser = argparse.ArgumentParser(
        description='Run test automation suite for g4j project'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '--output-dir',
        '-o',
        default='test_results',
        help='Directory for test reports (default: test_results)'
    )
    
    args = parser.parse_args()
    
    # Set environment variable for output directory
    os.environ['TEST_OUTPUT_DIR'] = args.output_dir
    
    print("=" * 70)
    print("g4j Project - Test Automation Suite")
    print("=" * 70)
    print(f"Output Directory: {args.output_dir}")
    print(f"Verbose Mode: {args.verbose}")
    print("=" * 70)
    
    # Run the tests
    try:
        run_tests()
        print("\n✓ Test execution completed successfully!")
        return 0
    except Exception as e:
        print(f"\n✗ Test execution failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
