#!/bin/bash
# Test Automation Execution Script

set -e

echo "=========================================="
echo "G4J Test Automation Suite"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3 to run tests."
    exit 1
fi

print_status "Python version: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 is not installed. Please install pip3 to install dependencies."
    exit 1
fi

# Install test dependencies if needed
if [ "$1" == "--install-deps" ]; then
    print_status "Installing test dependencies..."
    pip3 install -r requirements-test.txt
    print_status "Dependencies installed successfully!"
    echo ""
fi

# Parse command line arguments
TEST_TYPE="${1:-all}"
REPORT_FORMAT="${2:-console}"

print_status "Test Type: $TEST_TYPE"
print_status "Report Format: $REPORT_FORMAT"
echo ""

# Run tests based on type
case $TEST_TYPE in
    "all")
        print_status "Running all tests..."
        python3 test_automation_framework.py
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py -v
        else
            print_warning "pytest not found. Run with --install-deps to install."
        fi
        ;;
    
    "unit")
        print_status "Running unit tests only..."
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py -v -m unit
        else
            python3 test_automation_framework.py
        fi
        ;;
    
    "integration")
        print_status "Running integration tests only..."
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py -v -m integration
        else
            print_warning "pytest not found. Run with --install-deps to install."
        fi
        ;;
    
    "smoke")
        print_status "Running smoke tests only..."
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py -v -m smoke
        else
            print_warning "pytest not found. Run with --install-deps to install."
        fi
        ;;
    
    "coverage")
        print_status "Running tests with coverage report..."
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py --cov=. --cov-report=html --cov-report=term
            print_status "Coverage report generated in htmlcov/index.html"
        else
            print_warning "pytest not found. Run with --install-deps to install."
        fi
        ;;
    
    "framework")
        print_status "Running custom test framework..."
        python3 test_automation_framework.py
        ;;
    
    "quick")
        print_status "Running quick tests (excluding slow tests)..."
        if command -v pytest &> /dev/null; then
            pytest pytest_tests.py -v -m "not slow"
        else
            python3 test_automation_framework.py
        fi
        ;;
    
    *)
        print_error "Unknown test type: $TEST_TYPE"
        echo ""
        echo "Usage: $0 [TEST_TYPE] [REPORT_FORMAT]"
        echo ""
        echo "TEST_TYPES:"
        echo "  all           - Run all tests (default)"
        echo "  unit          - Run unit tests only"
        echo "  integration   - Run integration tests only"
        echo "  smoke         - Run smoke tests only"
        echo "  coverage      - Run tests with coverage report"
        echo "  framework     - Run custom test framework"
        echo "  quick         - Run quick tests (exclude slow tests)"
        echo "  --install-deps - Install test dependencies"
        echo ""
        echo "REPORT_FORMATS:"
        echo "  console       - Console output (default)"
        echo "  json          - JSON format"
        echo "  html          - HTML format"
        exit 1
        ;;
esac

echo ""
print_status "Test execution completed!"

# Check if test report was generated
if [ -f "final_test_report.json" ]; then
    print_status "Test report available: final_test_report.json"
fi

if [ -f "test_report.json" ]; then
    print_status "Test report available: test_report.json"
fi

exit 0
