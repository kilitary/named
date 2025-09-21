#!/usr/bin/env python3
"""
Test for 0 level counter-error grouped nodes functionality in response_prover_mock.py
"""

import os
import tempfile
from response_prover_mock import ResponseProverMock


def test_grouped_nodes_detection():
    """Test that grouped nodes scenarios are properly detected"""
    
    # Test case 1: Original mail2fbi.txt should trigger grouped nodes detection
    print("=== Test 1: Original mail2fbi.txt ===")
    prover = ResponseProverMock(repository_path="/home/runner/work/named/named")
    is_grouped = prover._detect_grouped_nodes_scenario()
    print(f"Grouped nodes detected: {is_grouped}")
    
    response = prover._generate_fsb_response()
    print(f"Response type: {'GROUPED NODES' if 'GROUPED NODES PROTOCOL' in response else 'STANDARD'}")
    print()
    
    # Test case 2: Create a non-grouped scenario 
    print("=== Test 2: Non-grouped scenario ===")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Simple email about weather and normal topics.")
        tmp_path = tmp.name
    
    try:
        prover_simple = ResponseProverMock(repository_path="/home/runner/work/named/named", mail_file=tmp_path)
        is_grouped_simple = prover_simple._detect_grouped_nodes_scenario()
        print(f"Grouped nodes detected: {is_grouped_simple}")
        
        response_simple = prover_simple._generate_fsb_response()
        print(f"Response type: {'GROUPED NODES' if 'GROUPED NODES PROTOCOL' in response_simple else 'STANDARD'}")
        print()
    finally:
        os.unlink(tmp_path)
    
    # Test case 3: Edge case with grouped indicators but no level 0 indicators
    print("=== Test 3: Grouped indicators only ===")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Multiple servers in group are running slowly. All computers seem affected.")
        tmp_path = tmp.name
    
    try:
        prover_group_only = ResponseProverMock(repository_path="/home/runner/work/named/named", mail_file=tmp_path)
        is_grouped_only = prover_group_only._detect_grouped_nodes_scenario()
        print(f"Grouped nodes detected: {is_grouped_only}")
        print()
    finally:
        os.unlink(tmp_path)
    
    # Test case 4: Edge case with level 0 indicators but no grouped indicators
    print("=== Test 4: Level 0 indicators only ===")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Single system has rootkit with ring-0 access and kernel level compromise.")
        tmp_path = tmp.name
    
    try:
        prover_level_only = ResponseProverMock(repository_path="/home/runner/work/named/named", mail_file=tmp_path)
        is_level_only = prover_level_only._detect_grouped_nodes_scenario()
        print(f"Grouped nodes detected: {is_level_only}")
        print()
    finally:
        os.unlink(tmp_path)

    # Test case 5: Combined indicators should trigger
    print("=== Test 5: Combined indicators ===")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write("Multiple systems with grouped nodes compromised by rootkit with ring-0 kernel level access.")
        tmp_path = tmp.name
    
    try:
        prover_combined = ResponseProverMock(repository_path="/home/runner/work/named/named", mail_file=tmp_path)
        is_combined = prover_combined._detect_grouped_nodes_scenario()
        print(f"Grouped nodes detected: {is_combined}")
        
        response_combined = prover_combined._generate_fsb_response()
        print(f"Response type: {'GROUPED NODES' if 'GROUPED NODES PROTOCOL' in response_combined else 'STANDARD'}")
        print()
    finally:
        os.unlink(tmp_path)


def test_simulation_pattern_analysis():
    """Test that simulation patterns are properly analyzed"""
    print("=== Simulation Pattern Analysis ===")
    prover = ResponseProverMock(repository_path="/home/runner/work/named/named")
    
    patterns = prover.simulation_patterns
    print(f"FSB responses found: {len(patterns.get('fsb_responses', []))}")
    print(f"Security keywords: {len(patterns.get('security_keywords', []))}")
    print(f"Grouped node patterns: {len(patterns.get('grouped_node_patterns', []))}")
    print(f"Level 0 instructions: {len(patterns.get('level_zero_instructions', []))}")
    
    if patterns.get('level_zero_instructions'):
        print("Sample level 0 instructions:", patterns['level_zero_instructions'][:2])
    if patterns.get('grouped_node_patterns'):
        print("Sample grouped patterns:", patterns['grouped_node_patterns'][:2])


def run_tests():
    """Run all tests"""
    print("🧪 Testing 0 Level Counter-Error Grouped Nodes Functionality")
    print("=" * 60)
    
    test_grouped_nodes_detection()
    test_simulation_pattern_analysis()
    
    print("✅ All tests completed!")


if __name__ == "__main__":
    run_tests()