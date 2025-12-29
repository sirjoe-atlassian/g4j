@echo off
REM Test execution script for automation framework (Windows)

echo ======================================
echo Test Automation Framework Execution
echo ======================================

set TEST_TYPE=all
set MARKERS=
set PARALLEL=

:parse_args
if "%1"=="" goto end_parse
if "%1"=="--smoke" (
    set MARKERS=-m smoke
    set TEST_TYPE=smoke
    shift
    goto parse_args
)
if "%1"=="--regression" (
    set MARKERS=-m regression
    set TEST_TYPE=regression
    shift
    goto parse_args
)
if "%1"=="--unit" (
    set MARKERS=-m unit
    set TEST_TYPE=unit
    shift
    goto parse_args
)
if "%1"=="--integration" (
    set MARKERS=-m integration
    set TEST_TYPE=integration
    shift
    goto parse_args
)
if "%1"=="--parallel" (
    set PARALLEL=-n auto
    shift
    goto parse_args
)
:end_parse

echo Running %TEST_TYPE% tests...

REM Install dependencies if needed
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Create necessary directories
if not exist "logs" mkdir logs
if not exist "reports" mkdir reports
if not exist "screenshots" mkdir screenshots
if not exist "allure-results" mkdir allure-results

REM Run tests
echo Executing tests...
pytest %MARKERS% %PARALLEL%

echo ======================================
echo Test execution completed!
echo ======================================
