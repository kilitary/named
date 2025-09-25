#!/usr/bin/env python3
"""
Playground Runner - Integration with SKYNET Research
====================================================

Simple runner to integrate Skynet Playground with existing SKYNET research infrastructure.
Provides easy access to the 4-step structured process from other components.
"""

import sys
import os
from pathlib import Path

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from skynet_playground import SkynetPlayground


def run_playground_session(data_source=None, verbose=True):
    """
    Run a complete playground session
    
    Args:
        data_source: Optional path to data source file
        verbose: Whether to print verbose output
        
    Returns:
        bool: Success status
    """
    if not verbose:
        # Redirect stdout to suppress verbose output
        import io
        import contextlib
        
        with contextlib.redirect_stdout(io.StringIO()):
            playground = SkynetPlayground(data_source)
            return playground.execute()
    else:
        playground = SkynetPlayground(data_source)
        return playground.execute()


def quick_analysis():
    """Quick analysis using synthetic data"""
    print("🔬 Quick Playground Analysis")
    playground = SkynetPlayground("synthetic")
    return playground.execute()


def main():
    """Main runner function"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "quick":
            success = quick_analysis()
        elif command == "silent":
            data_source = sys.argv[2] if len(sys.argv) > 2 else None
            success = run_playground_session(data_source, verbose=False)
            if success:
                print("✅ Playground session completed successfully")
            else:
                print("❌ Playground session failed")
        else:
            # Treat first argument as data source
            success = run_playground_session(sys.argv[1])
    else:
        # Default: run with automatic data source detection
        success = run_playground_session()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()