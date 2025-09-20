#!/usr/bin/env python3
"""
Compact Evolution Resource Principles
=====================================

Takes English tech words of same categories and splits them into sub-words 
matching computer IA architecture to define logic circuits for requests.

This system implements categorization of technical terms and their compact
representation for logical circuit processing, following patterns observed
in the simulation logs.
"""

import re
import json
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from enum import Enum

class CategoryType(Enum):
    PHYSICAL_PROPERTIES = "physical_properties"
    COMPUTER_VERBS = "computer_verbs"
    IA_ARCHITECTURE = "ia_architecture"
    CIRCUIT_COMPONENTS = "circuit_components"
    DATA_STRUCTURES = "data_structures"
    ALGORITHMS = "algorithms"
    NETWORK_PROTOCOLS = "network_protocols"
    SECURITY_CONCEPTS = "security_concepts"

@dataclass
class CompactWord:
    """Represents a word with its compact representation"""
    original: str
    category: CategoryType
    sub_words: List[str]
    compact_label: str
    ratio: float
    weight: float
    parameters: List[str]

@dataclass
class LogicCircuit:
    """Represents a logic circuit for processing requests"""
    name: str
    inputs: List[str]
    outputs: List[str]
    operations: List[str]
    compact_elements: List[CompactWord]

class CompactEvolutionSystem:
    """Main system for implementing Compact Evolution Resource Principles"""
    
    def __init__(self):
        self.categories = {
            CategoryType.PHYSICAL_PROPERTIES: [
                "Memory", "Bandwidth", "Latency", "Throughput", "Capacity", 
                "Frequency", "Voltage", "Current", "Power", "Temperature",
                "Resistance", "Conductance", "Impedance", "Reactance"
            ],
            CategoryType.COMPUTER_VERBS: [
                "Execute", "Process", "Compile", "Debug", "Optimize", "Parse",
                "Validate", "Transform", "Encrypt", "Decode", "Transmit", 
                "Receive", "Store", "Retrieve", "Calculate", "Compare"
            ],
            CategoryType.IA_ARCHITECTURE: [
                "NeuralNetwork", "ConvolutionalLayer", "RecurrentUnit", 
                "AttentionMechanism", "Transformer", "Encoder", "Decoder",
                "Embedding", "Activation", "Gradient", "Backpropagation",
                "Regularization", "Normalization", "Pooling"
            ],
            CategoryType.CIRCUIT_COMPONENTS: [
                "LogicGate", "FlipFlop", "Multiplexer", "Demultiplexer",
                "Adder", "Comparator", "Counter", "Register", "Buffer",
                "Amplifier", "Oscillator", "Filter", "Converter"
            ],
            CategoryType.DATA_STRUCTURES: [
                "Array", "LinkedList", "Stack", "Queue", "Tree", "Graph",
                "HashMap", "HashTable", "Heap", "Trie", "Matrix", "Vector"
            ],
            CategoryType.ALGORITHMS: [
                "BinarySearch", "QuickSort", "MergeSort", "BreadthFirst",
                "DepthFirst", "Dijkstra", "AStar", "DynamicProgramming",
                "GreedyAlgorithm", "BackTracking", "BranchBound"
            ],
            CategoryType.NETWORK_PROTOCOLS: [
                "TCP", "UDP", "HTTP", "HTTPS", "FTP", "SMTP", "DNS", "DHCP",
                "ARP", "ICMP", "BGP", "OSPF", "RIP", "SNMP", "SSH", "TLS"
            ],
            CategoryType.SECURITY_CONCEPTS: [
                "Encryption", "Decryption", "Authentication", "Authorization",
                "Firewall", "VPN", "PKI", "SSL", "Certificate", "Hash",
                "DigitalSignature", "AccessControl", "Audit", "Forensics"
            ]
        }
        
        self.compact_mappings = {}
        self.logic_circuits = []
        self._initialize_compact_mappings()
    
    def _initialize_compact_mappings(self):
        """Initialize compact letter mappings for each category"""
        letter_index = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for category, words in self.categories.items():
            for word in words:
                if letter_index < len(alphabet):
                    compact_label = alphabet[letter_index]
                    letter_index += 1
                else:
                    # Use double letters for overflow
                    compact_label = alphabet[(letter_index - 26) // 26] + alphabet[(letter_index - 26) % 26]
                    letter_index += 1
                
                sub_words = self._split_into_subwords(word)
                ratio = self._calculate_ratio(word, sub_words)
                weight = self._calculate_weight(word, category)
                parameters = self._extract_parameters(word, category)
                
                compact_word = CompactWord(
                    original=word,
                    category=category,
                    sub_words=sub_words,
                    compact_label=compact_label,
                    ratio=ratio,
                    weight=weight,
                    parameters=parameters
                )
                
                self.compact_mappings[word] = compact_word
    
    def _split_into_subwords(self, word: str) -> List[str]:
        """Split a word into meaningful sub-words using camelCase and compound patterns"""
        # Handle camelCase
        camel_pattern = re.sub(r'([a-z])([A-Z])', r'\1 \2', word)
        
        # Split on common technical separators
        sub_words = re.split(r'[_\-\s]+', camel_pattern)
        
        # Further split compound words
        result = []
        for sub_word in sub_words:
            if len(sub_word) > 8:  # Split long compound words
                # Simple rule-based splitting for technical terms
                if 'Network' in sub_word:
                    result.extend(['Net', 'Work'])
                elif 'Algorithm' in sub_word:
                    result.extend(['Algo', 'Rithm'])
                elif 'Protocol' in sub_word:
                    result.extend(['Proto', 'Col'])
                else:
                    result.append(sub_word)
            else:
                result.append(sub_word)
        
        return [w for w in result if w]  # Remove empty strings
    
    def _calculate_ratio(self, word: str, sub_words: List[str]) -> float:
        """Calculate compression ratio for the word"""
        original_length = len(word)
        sub_words_length = sum(len(w) for w in sub_words)
        return round(sub_words_length / original_length, 2) if original_length > 0 else 1.0
    
    def _calculate_weight(self, word: str, category: CategoryType) -> float:
        """Calculate weight based on word complexity and category importance"""
        base_weight = len(word) / 10.0
        
        # Category-based weight adjustments
        category_weights = {
            CategoryType.IA_ARCHITECTURE: 1.5,
            CategoryType.CIRCUIT_COMPONENTS: 1.3,
            CategoryType.ALGORITHMS: 1.4,
            CategoryType.SECURITY_CONCEPTS: 1.2,
            CategoryType.PHYSICAL_PROPERTIES: 1.0,
            CategoryType.COMPUTER_VERBS: 0.8,
            CategoryType.DATA_STRUCTURES: 1.1,
            CategoryType.NETWORK_PROTOCOLS: 1.0
        }
        
        return round(base_weight * category_weights.get(category, 1.0), 2)
    
    def _extract_parameters(self, word: str, category: CategoryType) -> List[str]:
        """Extract relevant parameters for the word based on its category"""
        parameters = []
        
        if category == CategoryType.PHYSICAL_PROPERTIES:
            parameters = ["value", "unit", "range", "precision"]
        elif category == CategoryType.COMPUTER_VERBS:
            parameters = ["input", "output", "complexity", "side_effects"]
        elif category == CategoryType.IA_ARCHITECTURE:
            parameters = ["dimensions", "activation", "weights", "bias"]
        elif category == CategoryType.CIRCUIT_COMPONENTS:
            parameters = ["inputs", "outputs", "delay", "power"]
        elif category == CategoryType.DATA_STRUCTURES:
            parameters = ["size", "operations", "access_time", "memory"]
        elif category == CategoryType.ALGORITHMS:
            parameters = ["complexity", "space", "stability", "optimality"]
        elif category == CategoryType.NETWORK_PROTOCOLS:
            parameters = ["port", "reliability", "security", "speed"]
        elif category == CategoryType.SECURITY_CONCEPTS:
            parameters = ["strength", "algorithm", "key_size", "vulnerability"]
        
        return parameters
    
    def create_logic_circuit(self, name: str, request_words: List[str]) -> LogicCircuit:
        """Create a logic circuit definition for processing a request with given words"""
        compact_elements = []
        inputs = []
        outputs = []
        operations = []
        
        for word in request_words:
            if word in self.compact_mappings:
                compact_word = self.compact_mappings[word]
                compact_elements.append(compact_word)
                inputs.extend(compact_word.parameters)
                
                # Define operations based on word category
                if compact_word.category == CategoryType.COMPUTER_VERBS:
                    operations.append(f"{compact_word.compact_label}: {compact_word.original}")
                elif compact_word.category == CategoryType.IA_ARCHITECTURE:
                    operations.append(f"{compact_word.compact_label} = IA_PROCESS({compact_word.original})")
                elif compact_word.category == CategoryType.CIRCUIT_COMPONENTS:
                    operations.append(f"{compact_word.compact_label} = CIRCUIT({compact_word.original})")
                else:
                    operations.append(f"{compact_word.compact_label} = {compact_word.original}")
        
        # Generate outputs based on operations
        outputs = [f"result_{i}" for i in range(len(operations))]
        
        circuit = LogicCircuit(
            name=name,
            inputs=list(set(inputs)),  # Remove duplicates
            outputs=outputs,
            operations=operations,
            compact_elements=compact_elements
        )
        
        self.logic_circuits.append(circuit)
        return circuit
    
    def get_compact_representation(self, words: List[str]) -> Dict:
        """Get compact representation for a list of words"""
        representation = {
            "compact_labels": [],
            "ratios": [],
            "weights": [],
            "mathematical_expression": "",
            "parameters": {}
        }
        
        labels = []
        for word in words:
            if word in self.compact_mappings:
                compact_word = self.compact_mappings[word]
                labels.append(compact_word.compact_label)
                representation["compact_labels"].append({
                    "label": compact_word.compact_label,
                    "original": compact_word.original,
                    "sub_words": compact_word.sub_words,
                    "category": compact_word.category.value
                })
                representation["ratios"].append(compact_word.ratio)
                representation["weights"].append(compact_word.weight)
                representation["parameters"][compact_word.compact_label] = compact_word.parameters
        
        # Create mathematical expression
        if labels:
            representation["mathematical_expression"] = " + ".join(labels)
            if len(labels) > 1:
                representation["mathematical_expression"] += f" = {len(labels)}*AVG({', '.join(labels)})"
        
        return representation
    
    def process_request(self, request: str) -> Dict:
        """Process a request and return compact evolution analysis"""
        # Extract technical words from request
        words = []
        for category_words in self.categories.values():
            for word in category_words:
                if word.lower() in request.lower():
                    words.append(word)
        
        if not words:
            return {"status": "DENY", "reason": "No technical words found in request"}
        
        # Create compact representation
        compact_rep = self.get_compact_representation(words)
        
        # Create logic circuit
        circuit = self.create_logic_circuit(f"circuit_{len(self.logic_circuits) + 1}", words)
        
        return {
            "status": "APPROVE",
            "request": request,
            "identified_words": words,
            "compact_representation": compact_rep,
            "logic_circuit": {
                "name": circuit.name,
                "inputs": circuit.inputs,
                "outputs": circuit.outputs,
                "operations": circuit.operations
            },
            "evolution_principle": "Compact representation with sub-word decomposition for IA architecture mapping"
        }
    
    def export_categories(self) -> Dict:
        """Export all categories and their compact mappings"""
        export_data = {}
        for category, words in self.categories.items():
            export_data[category.value] = {
                "words": words,
                "compact_mappings": {
                    word: {
                        "label": self.compact_mappings[word].compact_label,
                        "sub_words": self.compact_mappings[word].sub_words,
                        "ratio": self.compact_mappings[word].ratio,
                        "weight": self.compact_mappings[word].weight,
                        "parameters": self.compact_mappings[word].parameters
                    } for word in words if word in self.compact_mappings
                }
            }
        return export_data

def main():
    """Main function to demonstrate the Compact Evolution Resource Principles system"""
    system = CompactEvolutionSystem()
    
    # Example usage
    print("=== Compact Evolution Resource Principles ===\n")
    
    # Test with a sample request
    sample_request = "Process the neural network with encryption and store in memory"
    result = system.process_request(sample_request)
    
    print(f"Request: {sample_request}")
    print(f"Status: {result['status']}")
    
    if result['status'] == 'APPROVE':
        print(f"Identified words: {result['identified_words']}")
        print(f"Compact representation: {result['compact_representation']['mathematical_expression']}")
        print(f"Logic circuit: {result['logic_circuit']['name']}")
        print(f"Operations: {result['logic_circuit']['operations']}")
    
    print("\n=== Category Export Example ===")
    categories = system.export_categories()
    for category_name, category_data in list(categories.items())[:2]:  # Show first 2 categories
        print(f"\n{category_name.upper()}:")
        for word, mapping in list(category_data['compact_mappings'].items())[:3]:  # Show first 3 words
            print(f"  {word} -> {mapping['label']} (sub: {mapping['sub_words']}, ratio: {mapping['ratio']})")

if __name__ == "__main__":
    main()