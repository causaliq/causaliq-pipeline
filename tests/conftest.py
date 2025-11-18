"""
Pytest configuration for causaliq-workflow tests.

Sets up the Python path to include test fixtures.
"""

import sys
from pathlib import Path

# Add functional test fixtures to Python path so test_action can be imported
fixtures_dir = Path(__file__).parent / "functional" / "fixtures"
if str(fixtures_dir) not in sys.path:
    sys.path.insert(0, str(fixtures_dir))
