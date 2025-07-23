#!/usr/bin/env python3
"""
Test runner script for the Linkbar Python SDK

Usage:
    python run_tests.py              # Run unit tests only
    python run_tests.py --integration # Run integration tests (requires API key)
    python run_tests.py --all         # Run all tests
    python run_tests.py --coverage    # Run with coverage report
"""

import sys
import subprocess
import os


def run_command(cmd):
    """Run a command and return the exit code"""
    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd)


def main():
    args = sys.argv[1:]
    
    # Base pytest command
    cmd = ['python', '-m', 'pytest']
    
    if '--integration' in args:
        # Run only integration tests
        cmd.extend(['-m', 'integration'])
        if not os.getenv('LINKBAR_TEST_API_KEY'):
            print("WARNING: LINKBAR_TEST_API_KEY not set. Integration tests will be skipped.")
    elif '--all' in args:
        # Run all tests
        pass  # No additional filters
    else:
        # Run only unit tests (default)
        cmd.extend(['-m', 'not integration'])
    
    if '--coverage' in args:
        cmd.extend(['--cov=linkbar', '--cov-report=html', '--cov-report=term'])
    
    # Add verbose output
    cmd.append('-v')
    
    exit_code = run_command(cmd)
    
    if exit_code == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit code {exit_code}")
    
    return exit_code


if __name__ == '__main__':
    sys.exit(main())