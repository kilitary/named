#!/usr/bin/env python3
"""
Test script for infrastructure terminology classification and abbreviation splitting enhancements.

This script validates:
1. Enhanced infrastructure abbreviation splitting
2. Extended infrastructure terms classification
3. Improved compound word decomposition
4. Integration with response prover mock
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Red&Queen'))

from compact_evolution import CompactEvolutionSystem
from response_prover_mock import ResponseProverMock, VerbCategory

def test_infrastructure_abbreviations():
    """Test enhanced infrastructure abbreviation splitting"""
    print("=== Testing Infrastructure Abbreviation Splitting ===")
    system = CompactEvolutionSystem()
    
    # Test new infrastructure abbreviations
    test_cases = {
        'VPC': ['Virtual', 'Private', 'Cloud'],
        'K8S': ['Kubernetes'],
        'CICD': ['CI', 'CD'],
        'APM': ['App', 'Perf', 'Monitor'],
        'SDN': ['Soft', 'Defined', 'Net'],
        'RDBMS': ['Rel', 'DB', 'Mgmt', 'System'],
        'IOT': ['Internet', 'Of', 'Things'],
        'NVME': ['Non', 'Volatile', 'Mem', 'Express'],
        'SIEM': ['Security', 'Info', 'Event', 'Mgmt'],
        'SOAR': ['Security', 'Orch', 'Auto', 'Resp'],
        'OAUTH': ['Open', 'Auth'],
        'VLAN': ['Virtual', 'LAN'],
        'MPLS': ['Multi', 'Proto', 'Label', 'Switch'],
        'OLTP': ['Online', 'Trans', 'Proc'],
        'CRUD': ['Create', 'Read', 'Update', 'Delete']
    }
    
    passed = 0
    failed = 0
    
    for abbr, expected in test_cases.items():
        result = system._split_into_subwords(abbr)
        if result == expected:
            print(f"✓ {abbr} -> {result}")
            passed += 1
        else:
            print(f"✗ {abbr} -> {result} (expected: {expected})")
            failed += 1
    
    print(f"\nAbbreviation tests: {passed} passed, {failed} failed")
    return failed == 0

def test_compound_word_splitting():
    """Test enhanced compound word splitting"""
    print("\n=== Testing Compound Word Splitting ===")
    system = CompactEvolutionSystem()
    
    test_cases = {
        'Kubernetes': ['Kube', 'rnetes'],
        'Microservice': ['Micro', 'service'],
        'Authentication': ['Auth', 'entication'],
        'Orchestration': ['Orch', 'estration'],
        'Virtualization': ['Virtual', 'ization'],
        'Configuration': ['Config', 'uration'],
        'Infrastructure': ['Infra', 'structure'],
        'Authorization': ['Author', 'ization'],
        'Performance': ['Perform', 'ance'],
        'Bandwidth': ['Band', 'width'],
        'Throughput': ['Through', 'put'],
        'Encryption': ['Encrypt', 'ion'],
        'Serverless': ['Server', 'less'],
        'Distributed': ['Distrib', 'uted'],
        'Scalability': ['Scale', 'ability'],
        'Availability': ['Avail', 'ability'],
        'Observability': ['Observe', 'ability']
    }
    
    passed = 0
    failed = 0
    
    for word, expected in test_cases.items():
        result = system._split_into_subwords(word)
        if result == expected:
            print(f"✓ {word} -> {result}")
            passed += 1
        else:
            print(f"✗ {word} -> {result} (expected: {expected})")
            failed += 1
    
    print(f"\nCompound word tests: {passed} passed, {failed} failed")
    return failed == 0

def test_infrastructure_terms_classification():
    """Test enhanced infrastructure terms classification in response prover"""
    print("\n=== Testing Infrastructure Terms Classification ===")
    prover = ResponseProverMock()
    
    # Test content with various infrastructure terms
    test_content = """
    The cloud infrastructure deployment includes kubernetes orchestration, 
    microservice architecture, and distributed authentication systems with 
    load balancing, monitoring, and observability features. The network 
    topology includes virtual private clouds, software-defined networking,
    container orchestration, database replication, and security monitoring.
    """
    
    verb_analysis = prover._analyze_verbs_logic(test_content)
    
    # Count infrastructure terms detected
    infrastructure_terms = []
    for result in verb_analysis:
        if VerbCategory.INFRASTRUCTURE_TERMS in result.categories:
            infrastructure_terms.append(result.verb)
    
    print(f"Infrastructure terms detected: {len(infrastructure_terms)}")
    print(f"Terms: {sorted(set(infrastructure_terms))}")
    
    # Check for key infrastructure terms
    expected_terms = ['infrastructure', 'orchestration', 'microservice', 'distributed', 
                     'authentication', 'load', 'balancing', 'monitoring', 'observability',
                     'network', 'topology', 'virtual', 'container', 'database', 'replication']
    
    found_terms = set(infrastructure_terms)
    detected_expected = [term for term in expected_terms if term in found_terms]
    
    print(f"Expected infrastructure terms detected: {len(detected_expected)}/{len(expected_terms)}")
    print(f"Detected: {detected_expected}")
    
    # Should detect at least 80% of expected terms
    success_rate = len(detected_expected) / len(expected_terms)
    return success_rate >= 0.8

def test_integration():
    """Test integration between systems"""
    print("\n=== Testing System Integration ===")
    
    # Test compact evolution system with infrastructure terms
    system = CompactEvolutionSystem()
    
    # Process a request with infrastructure terminology
    request = "Deploy kubernetes cluster with microservice architecture and monitoring"
    result = system.process_request(request)
    
    print(f"Request processing status: {result['status']}")
    print(f"Identified items: {len(result['identified_words'])}")
    
    # Check if infrastructure terms are properly categorized
    infrastructure_items = [word for word in result['identified_words'] 
                          if any(infra_term in word.lower() for infra_term in 
                                ['kubernetes', 'microservice', 'monitoring', 'cluster', 'deploy'])]
    
    print(f"Infrastructure-related items: {len(infrastructure_items)}")
    
    return result['status'] == 'APPROVE' and len(infrastructure_items) > 0

def main():
    """Run all tests"""
    print("Infrastructure Terminology Classification and Abbreviation Splitting Tests")
    print("=" * 80)
    
    tests = [
        test_infrastructure_abbreviations,
        test_compound_word_splitting,
        test_infrastructure_terms_classification,
        test_integration
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
                print("✓ PASSED\n")
            else:
                print("✗ FAILED\n")
        except Exception as e:
            print(f"✗ ERROR: {e}\n")
    
    print("=" * 80)
    print(f"Overall Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All infrastructure enhancements working correctly!")
        return 0
    else:
        print("⚠️  Some tests failed - check implementation")
        return 1

if __name__ == "__main__":
    sys.exit(main())