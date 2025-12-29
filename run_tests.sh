#!/bin/bash
# Test execution script for automation framework

echo "======================================"
echo "Test Automation Framework Execution"
echo "======================================"

# Default values
TEST_TYPE="all"
MARKERS=""
PARALLEL=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --smoke)
            MARKERS="-m smoke"
            TEST_TYPE="smoke"
            shift
            ;;
        --regression)
            MARKERS="-m regression"
            TEST_TYPE="regression"
            shift
            ;;
        --unit)
            MARKERS="-m unit"
            TEST_TYPE="unit"
            shift
            ;;
        --integration)
            MARKERS="-m integration"
            TEST_TYPE="integration"
            shift
            ;;
        --parallel)
            PARALLEL="-n auto"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: ./run_tests.sh [--smoke|--regression|--unit|--integration] [--parallel]"
            exit 1
            ;;
    esac
done

echo "Running $TEST_TYPE tests..."

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Create necessary directories
mkdir -p logs reports screenshots allure-results

# Run tests
echo "Executing tests..."
pytest $MARKERS $PARALLEL

echo "======================================"
echo "Test execution completed!"
echo "======================================"
