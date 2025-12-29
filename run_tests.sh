#!/bin/bash

# Test Automation Runner Script
# Usage: ./run_tests.sh [test_type] [options]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Test Automation Framework${NC}"
echo -e "${GREEN}================================${NC}"
echo ""

# Parse arguments
TEST_TYPE=${1:-all}
PARALLEL=${2:-false}

# Function to run tests
run_tests() {
    local marker=$1
    local description=$2
    
    echo -e "${YELLOW}Running $description...${NC}"
    
    if [ "$PARALLEL" == "parallel" ]; then
        pytest -m "$marker" -n auto
    else
        pytest -m "$marker"
    fi
}

# Run tests based on type
case $TEST_TYPE in
    unit)
        run_tests "unit" "Unit Tests"
        ;;
    integration)
        run_tests "integration" "Integration Tests"
        ;;
    e2e)
        run_tests "e2e" "End-to-End Tests"
        ;;
    smoke)
        run_tests "smoke" "Smoke Tests"
        ;;
    regression)
        run_tests "regression" "Regression Tests"
        ;;
    api)
        run_tests "api" "API Tests"
        ;;
    all)
        echo -e "${YELLOW}Running All Tests...${NC}"
        if [ "$PARALLEL" == "parallel" ]; then
            pytest -n auto
        else
            pytest
        fi
        ;;
    *)
        echo -e "${RED}Invalid test type: $TEST_TYPE${NC}"
        echo "Usage: ./run_tests.sh [unit|integration|e2e|smoke|regression|api|all] [parallel]"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}Test execution completed!${NC}"
echo -e "${GREEN}Check reports/ directory for detailed results.${NC}"
