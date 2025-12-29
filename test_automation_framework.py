"""
Test Automation Framework for g4j Project
Created for Jira Issue: DEV-4 - Test automation generate code
"""

import unittest
import json
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TestResult:
    """Data class to store test execution results"""
    test_name: str
    status: str  # 'PASSED', 'FAILED', 'SKIPPED'
    execution_time: float
    error_message: Optional[str] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test result to dictionary"""
        return {
            'test_name': self.test_name,
            'status': self.status,
            'execution_time': self.execution_time,
            'error_message': self.error_message,
            'timestamp': self.timestamp
        }


class TestReporter:
    """Handles test result reporting and logging"""
    
    def __init__(self, output_dir: str = 'test_results'):
        self.output_dir = output_dir
        self.results: List[TestResult] = []
        os.makedirs(output_dir, exist_ok=True)
    
    def add_result(self, result: TestResult):
        """Add a test result to the reporter"""
        self.results.append(result)
    
    def generate_report(self, format: str = 'json'):
        """Generate test report in specified format"""
        if format == 'json':
            return self._generate_json_report()
        elif format == 'html':
            return self._generate_html_report()
        else:
            return self._generate_text_report()
    
    def _generate_json_report(self) -> str:
        """Generate JSON format test report"""
        report_data = {
            'total_tests': len(self.results),
            'passed': sum(1 for r in self.results if r.status == 'PASSED'),
            'failed': sum(1 for r in self.results if r.status == 'FAILED'),
            'skipped': sum(1 for r in self.results if r.status == 'SKIPPED'),
            'results': [r.to_dict() for r in self.results]
        }
        
        report_path = os.path.join(self.output_dir, 'test_report.json')
        with open(report_path, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return report_path
    
    def _generate_html_report(self) -> str:
        """Generate HTML format test report"""
        passed = sum(1 for r in self.results if r.status == 'PASSED')
        failed = sum(1 for r in self.results if r.status == 'FAILED')
        skipped = sum(1 for r in self.results if r.status == 'SKIPPED')
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Test Automation Report - g4j</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .summary {{ background-color: #f0f0f0; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .passed {{ color: green; }}
        .failed {{ color: red; }}
        .skipped {{ color: orange; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Test Automation Report - g4j Project</h1>
    <div class="summary">
        <h2>Summary</h2>
        <p>Total Tests: {len(self.results)}</p>
        <p class="passed">Passed: {passed}</p>
        <p class="failed">Failed: {failed}</p>
        <p class="skipped">Skipped: {skipped}</p>
    </div>
    <h2>Test Results</h2>
    <table>
        <tr>
            <th>Test Name</th>
            <th>Status</th>
            <th>Execution Time (s)</th>
            <th>Error Message</th>
            <th>Timestamp</th>
        </tr>
"""
        
        for result in self.results:
            status_class = result.status.lower()
            error_msg = result.error_message if result.error_message else '-'
            html_content += f"""
        <tr>
            <td>{result.test_name}</td>
            <td class="{status_class}">{result.status}</td>
            <td>{result.execution_time:.3f}</td>
            <td>{error_msg}</td>
            <td>{result.timestamp}</td>
        </tr>
"""
        
        html_content += """
    </table>
</body>
</html>
"""
        
        report_path = os.path.join(self.output_dir, 'test_report.html')
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        return report_path
    
    def _generate_text_report(self) -> str:
        """Generate plain text format test report"""
        passed = sum(1 for r in self.results if r.status == 'PASSED')
        failed = sum(1 for r in self.results if r.status == 'FAILED')
        skipped = sum(1 for r in self.results if r.status == 'SKIPPED')
        
        report_lines = [
            "=" * 60,
            "Test Automation Report - g4j Project",
            "=" * 60,
            f"Total Tests: {len(self.results)}",
            f"Passed: {passed}",
            f"Failed: {failed}",
            f"Skipped: {skipped}",
            "=" * 60,
            "\nDetailed Results:",
            "-" * 60
        ]
        
        for result in self.results:
            report_lines.append(f"\nTest: {result.test_name}")
            report_lines.append(f"Status: {result.status}")
            report_lines.append(f"Execution Time: {result.execution_time:.3f}s")
            if result.error_message:
                report_lines.append(f"Error: {result.error_message}")
            report_lines.append(f"Timestamp: {result.timestamp}")
            report_lines.append("-" * 60)
        
        report_content = '\n'.join(report_lines)
        report_path = os.path.join(self.output_dir, 'test_report.txt')
        with open(report_path, 'w') as f:
            f.write(report_content)
        
        return report_path
    
    def print_summary(self):
        """Print test summary to console"""
        passed = sum(1 for r in self.results if r.status == 'PASSED')
        failed = sum(1 for r in self.results if r.status == 'FAILED')
        skipped = sum(1 for r in self.results if r.status == 'SKIPPED')
        
        print("\n" + "=" * 60)
        print("Test Execution Summary")
        print("=" * 60)
        print(f"Total Tests: {len(self.results)}")
        print(f"✓ Passed: {passed}")
        print(f"✗ Failed: {failed}")
        print(f"⊘ Skipped: {skipped}")
        print("=" * 60 + "\n")


class BaseTestCase(unittest.TestCase):
    """Base test case class with enhanced functionality"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        cls.reporter = TestReporter()
        print(f"\n{'=' * 60}")
        print(f"Starting Test Suite: {cls.__name__}")
        print(f"{'=' * 60}\n")
    
    @classmethod
    def tearDownClass(cls):
        """Tear down test class and generate reports"""
        print(f"\n{'=' * 60}")
        print(f"Completed Test Suite: {cls.__name__}")
        print(f"{'=' * 60}\n")
        
        cls.reporter.print_summary()
        
        # Generate reports in all formats
        json_report = cls.reporter.generate_report('json')
        html_report = cls.reporter.generate_report('html')
        text_report = cls.reporter.generate_report('text')
        
        print(f"Reports generated:")
        print(f"  - JSON: {json_report}")
        print(f"  - HTML: {html_report}")
        print(f"  - Text: {text_report}")


class SampleTestSuite(BaseTestCase):
    """Sample test suite demonstrating the framework usage"""
    
    def test_example_pass(self):
        """Example test that passes"""
        import time
        start_time = time.time()
        
        try:
            # Simulate test logic
            self.assertEqual(2 + 2, 4, "Basic math should work")
            self.assertTrue(True, "True should be true")
            
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_pass',
                status='PASSED',
                execution_time=execution_time
            )
            self.reporter.add_result(result)
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_pass',
                status='FAILED',
                execution_time=execution_time,
                error_message=str(e)
            )
            self.reporter.add_result(result)
            raise
    
    def test_example_with_assertion(self):
        """Example test with assertions"""
        import time
        start_time = time.time()
        
        try:
            # Test string operations
            test_string = "Hello, g4j!"
            self.assertIn("g4j", test_string)
            self.assertEqual(len(test_string), 11)
            
            # Test list operations
            test_list = [1, 2, 3, 4, 5]
            self.assertEqual(len(test_list), 5)
            self.assertIn(3, test_list)
            
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_with_assertion',
                status='PASSED',
                execution_time=execution_time
            )
            self.reporter.add_result(result)
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_with_assertion',
                status='FAILED',
                execution_time=execution_time,
                error_message=str(e)
            )
            self.reporter.add_result(result)
            raise
    
    def test_example_dictionary(self):
        """Example test for dictionary operations"""
        import time
        start_time = time.time()
        
        try:
            # Test dictionary operations
            test_dict = {'name': 'g4j', 'version': '1.0', 'type': 'project'}
            self.assertEqual(test_dict['name'], 'g4j')
            self.assertIn('version', test_dict)
            self.assertEqual(len(test_dict), 3)
            
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_dictionary',
                status='PASSED',
                execution_time=execution_time
            )
            self.reporter.add_result(result)
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = TestResult(
                test_name='test_example_dictionary',
                status='FAILED',
                execution_time=execution_time,
                error_message=str(e)
            )
            self.reporter.add_result(result)
            raise


def run_tests():
    """Main function to run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(SampleTestSuite)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    run_tests()
