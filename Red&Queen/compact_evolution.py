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
import math
import random
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from enum import Enum

# --- Console color support (random sub-word colorization) ---
try:
    # colorama enables ANSI colors on Windows consoles
    import colorama  # type: ignore
    colorama.just_fix_windows_console()
    _COLORAMA_OK = True
except Exception:
    _COLORAMA_OK = False

# A small palette cycling through readable foreground colors
_COLOR_CODES: List[int] = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]

def colorize_text(text: object) -> str:
    """Return text with colors changing randomly for sub-words of length 2..4.
    - Splits each line into random chunks of size 2..4 characters and applies a random color per chunk.
    - Preserves newlines and resets chunking at each newline.
    - Ensures consecutive chunks don't reuse the same color where possible.
    """
    s = str(text)
    if not s:
        return s

    def _pick_color(prev: Optional[int]) -> int:
        if prev is None:
            return random.choice(_COLOR_CODES)
        # Avoid repeating the same color if possible
        choices = [c for c in _COLOR_CODES if c != prev]
        return random.choice(choices) if choices else prev

    out: List[str] = []
    i = 0
    prev_code: Optional[int] = None
    n = len(s)

    while i < n:
        if s[i] == "\n":
            out.append("\n")
            i += 1
            prev_code = None
            continue
        # Determine remaining characters until next newline to keep chunks within a line
        next_nl = s.find("\n", i)
        line_end = next_nl if next_nl != -1 else n
        remaining = line_end - i
        if remaining <= 0:
            break
        # Random chunk length between 2 and 4, but not exceeding remaining
        chunk_len = min(random.randint(2, 4), remaining)
        # If only 1 char remains, color it as its own chunk
        if remaining == 1:
            chunk_len = 1
        code = _pick_color(prev_code)
        chunk = s[i:i + chunk_len]
        out.append(f"\033[{code}m{chunk}\033[0m")
        prev_code = code
        i += chunk_len

    return "".join(out)


def printc(*args, sep: str = " ", end: str = "\n") -> None:
    """Print with random per-chunk colorization across the entire assembled line.
    Behaves like print(), but colorizes the concatenated string.
    """
    line = sep.join(str(a) for a in args)
    print(colorize_text(line), end=end)


class CategoryType(Enum):
    PHYSICAL_PROPERTIES = "physical_properties"
    COMPUTER_VERBS = "computer_verbs"
    IA_ARCHITECTURE = "ia_architecture"
    CIRCUIT_COMPONENTS = "circuit_components"
    DATA_STRUCTURES = "data_structures"
    ALGORITHMS = "algorithms"
    NETWORK_PROTOCOLS = "network_protocols"
    SECURITY_CONCEPTS = "security_concepts"
    THREADING_CONCEPTS = "threading_concepts"  # New category for threading concepts


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
    operation_categories: List[CategoryType]  # parallel to operations


@dataclass
class ExecutionAxis:
    """Computer axis with optional hyperthreading for scheduling operations."""
    cores: int = 1
    threads_per_core: int = 2
    hyperthreading: bool = False

    def total_threads(self) -> int:
        return self.cores * (self.threads_per_core if self.hyperthreading else 1)

    def thread_ids(self) -> List[str]:
        if not self.hyperthreading:
            return ["C0_T0"]
        ids = []
        for c in range(self.cores):
            for t in range(self.threads_per_core):
                ids.append(f"C{c}_T{t}")
        return ids

    def schedule_round_robin_indices(self, indices: List[int]) -> Dict[str, List[int]]:
        """Round-robin assign a list of operation indices to available threads."""
        threads = self.thread_ids()
        if not threads:
            threads = ["C0_T0"]
        plan: Dict[str, List[int]] = {tid: [] for tid in threads}
        for i, idx in enumerate(indices):
            tid = threads[i % len(threads)]
            plan[tid].append(idx)
        return plan


@dataclass
class TimeAxis:
    """Time axis to model execution over an entire dataset via time slices."""
    timeslice_ms: int = 10
    dataset_size: int = 1
    chunk_size: int = 1  # how many items per timeslice per thread-op

    def compute_timeline(self, assignment_indices: Dict[str, List[int]], circuit: LogicCircuit) -> Dict:
        # Build quick lookup
        op_list = circuit.operations
        op_cats = circuit.operation_categories

        # Prepare thread-local time cursor and timeline
        cursor: Dict[str, int] = {tid: 0 for tid in assignment_indices}
        timeline: Dict[str, List[Dict]] = {tid: [] for tid in assignment_indices}

        total_chunks = max(1, math.ceil(self.dataset_size / max(1, self.chunk_size)))

        for tid, idx_list in assignment_indices.items():
            for idx in idx_list:
                op = op_list[idx]
                cat = op_cats[idx]
                if cat == CategoryType.COMPUTER_VERBS:
                    # Process entire dataset in chunks for verbs
                    for chunk in range(total_chunks):
                        start = cursor[tid]
                        end = start + self.timeslice_ms
                        start_item = chunk * self.chunk_size
                        end_item = min(self.dataset_size, (chunk + 1) * self.chunk_size) - 1
                        timeline[tid].append({
                            "op": op,
                            "category": cat.value,
                            "start_ms": start,
                            "end_ms": end,
                            "items": [start_item, max(start_item, end_item)]
                        })
                        cursor[tid] = end
                else:
                    # Non-verb ops: single setup slice
                    start = cursor[tid]
                    end = start + self.timeslice_ms
                    timeline[tid].append({
                        "op": op,
                        "category": cat.value,
                        "start_ms": start,
                        "end_ms": end,
                        "items": None
                    })
                    cursor[tid] = end

        estimated_total_time_ms = max(cursor.values()) if cursor else 0
        return {
            "timeslice_ms": self.timeslice_ms,
            "dataset_size": self.dataset_size,
            "chunk_size": self.chunk_size,
            "estimated_total_time_ms": estimated_total_time_ms,
            "timeline": timeline,
        }


class CompactEvolutionSystem:
    """Main system for implementing Compact Evolution Resource Principles"""

    def __init__(self) -> None:
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
            ],
            CategoryType.THREADING_CONCEPTS: [
                "Thread", "Process", "Hyperthread", "Concurrency", "Parallelism",
                "Mutex", "Semaphore", "Lock", "Unlock", "Join", "Detach",
                "Yield", "Sleep", "Wakeup", "Signal", "Broadcast"
            ]
        }

        self.compact_mappings = {}
        self.logic_circuits = []
        self.execution_axis = ExecutionAxis()  # computer axis
        self.time_axis = TimeAxis()            # time axis
        self._initialize_compact_mappings()

        # Track last total length of detected Computer Verbs to detect decay > 2.348x
        self._last_verb_total_len: Optional[int] = None

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
        elif category == CategoryType.THREADING_CONCEPTS:
            parameters = ["thread_id", "process_id", "priority", "affinity"]

        return parameters

    def create_logic_circuit(self, name: str, request_words: List[str]) -> LogicCircuit:
        """Create a logic circuit definition for processing a request with given words"""
        compact_elements = []
        inputs = []
        outputs = []
        operations = []
        op_categories: List[CategoryType] = []

        for word in request_words:
            if word in self.compact_mappings:
                compact_word = self.compact_mappings[word]
                compact_elements.append(compact_word)
                inputs.extend(compact_word.parameters)

                # Define operations based on word category
                if compact_word.category == CategoryType.COMPUTER_VERBS:
                    operations.append(f"{compact_word.compact_label}: {compact_word.original}")
                    op_categories.append(CategoryType.COMPUTER_VERBS)
                elif compact_word.category == CategoryType.IA_ARCHITECTURE:
                    operations.append(f"{compact_word.compact_label} = IA_PROCESS({compact_word.original})")
                    op_categories.append(CategoryType.IA_ARCHITECTURE)
                elif compact_word.category == CategoryType.CIRCUIT_COMPONENTS:
                    operations.append(f"{compact_word.compact_label} = CIRCUIT({compact_word.original})")
                    op_categories.append(CategoryType.CIRCUIT_COMPONENTS)
                else:
                    operations.append(f"{compact_word.compact_label} = {compact_word.original}")
                    op_categories.append(compact_word.category)

        # Generate outputs based on operations
        outputs = [f"result_{i}" for i in range(len(operations))]

        circuit = LogicCircuit(
            name=name,
            inputs=list(set(inputs)),  # Remove duplicates
            outputs=outputs,
            operations=operations,
            compact_elements=compact_elements,
            operation_categories=op_categories
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

    def enable_hyperthreading(self, enabled: bool = True, cores: int = 1, threads_per_core: int = 2):
        """Configure hyperthreading on the computer axis."""
        self.execution_axis.hyperthreading = bool(enabled)
        self.execution_axis.cores = max(1, int(cores))
        self.execution_axis.threads_per_core = max(1, int(threads_per_core))

    def configure_time_axis(self, timeslice_ms: int = 10, dataset_size: int = 1, chunk_size: int = 1):
        """Configure the time axis for dataset-wide processing."""
        self.time_axis.timeslice_ms = max(1, int(timeslice_ms))
        self.time_axis.dataset_size = max(1, int(dataset_size))
        self.time_axis.chunk_size = max(1, int(chunk_size))

    def _should_enable_hyperthreading(self, words: List[str]) -> bool:
        signal_words = {"hyperthread", "hyperthreading", "parallel", "parallelism", "concurrency", "thread"}
        wset = {w.lower() for w in words}
        return self.execution_axis.hyperthreading or any(w in wset for w in signal_words)

    def _plan_execution_and_time(self, circuit: LogicCircuit, words: List[str]) -> Tuple[Dict, Dict]:
        """Plan hyperthreaded execution for computer verbs and link to time axis over entire dataset."""
        ht = self._should_enable_hyperthreading(words)
        axis = self.execution_axis
        tids = axis.thread_ids() if ht else ["C0_T0"]

        # Identify indices of computer verbs
        verb_indices = [i for i, cat in enumerate(circuit.operation_categories) if cat == CategoryType.COMPUTER_VERBS]
        nonverb_indices = [i for i in range(len(circuit.operations)) if i not in verb_indices]

        if ht and verb_indices:
            assignment_indices = axis.schedule_round_robin_indices(verb_indices)
        else:
            assignment_indices = {tids[0]: verb_indices[:]}

        # Serialize non-verb ops on the primary thread
        if tids[0] not in assignment_indices:
            assignment_indices[tids[0]] = []
        assignment_indices[tids[0]].extend(nonverb_indices)

        # Also produce a human-readable mapping
        assignment_strings: Dict[str, List[str]] = {
            tid: [circuit.operations[i] for i in idxs] for tid, idxs in assignment_indices.items()
        }

        execution_plan = {
            "hyperthreading": ht,
            "cores": axis.cores,
            "threads_per_core": axis.threads_per_core if ht else 1,
            "total_threads": axis.total_threads() if ht else 1,
            "assignment_indices": assignment_indices,
            "assignment": assignment_strings,
        }

        # Time axis plan over the entire dataset
        time_plan = self.time_axis.compute_timeline(assignment_indices, circuit)
        return execution_plan, time_plan

    def _total_computer_verbs_length(self, words: List[str]) -> int:
        total = 0
        for w in words:
            cw = self.compact_mappings.get(w)
            if cw and cw.category == CategoryType.COMPUTER_VERBS:
                total += len(w)
        return total

    def _inject_parallel_if_decay(self, words: List[str]) -> Tuple[List[str], Optional[Dict]]:
        """If Computer Verbs' total length decreased > 2.348x vs last check, add 'Parallelism'."""
        curr = self._total_computer_verbs_length(words)
        trigger_info = None
        if self._last_verb_total_len is not None and curr > 0:
            factor = self._last_verb_total_len / curr
            if factor > 2.348:
                if "Parallelism" not in words:
                    words = words + ["Parallelism"]
                trigger_info = {
                    "trigger": "verb_length_decay",
                    "last_total": self._last_verb_total_len,
                    "current_total": curr,
                    "factor": round(factor, 3)
                }
        # Update history after check
        self._last_verb_total_len = curr
        return words, trigger_info

    def process_request(self, request: str) -> Dict:
        # 1) Detect words
        words: List[str] = []
        req_lc = request.lower()
        for category_words in self.categories.values():
            for word in category_words:
                if word.lower() in req_lc:
                    words.append(word)
        if not words:
            return {"status": "DENY", "reason": "No technical words found in request"}

        # Inject parallel meaning if verbs total length decayed > 2.348x
        words, trigger_info = self._inject_parallel_if_decay(words)

        # 2) Compact representation
        compact_rep = self.get_compact_representation(words)

        # 3) Build circuit
        circuit = self.create_logic_circuit(f"circuit_{len(self.logic_circuits) + 1}", words)

        # 4) Plan execution + time
        execution_plan, time_plan = self._plan_execution_and_time(circuit, words)

        result = {
            "status": "APPROVE",
            "request": request,
            "identified_words": words,
            "compact_representation": compact_rep,
            "logic_circuit": {
                "name": circuit.name,
                "inputs": circuit.inputs,
                "outputs": circuit.outputs,
                "operations": circuit.operations,
            },
            "execution_plan": execution_plan,
            "time_axis_plan": time_plan,
            "evolution_principle": "Compact representation with sub-word decomposition for IA architecture mapping",
        }
        if trigger_info:
            result["parallel_trigger"] = trigger_info
        return result

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

    # Configure axes: enable hyperthreading and set a dataset for the time axis
    system.enable_hyperthreading(True, cores=2, threads_per_core=2)
    system.configure_time_axis(timeslice_ms=5, dataset_size=20, chunk_size=5)

    printc("=== Compact Evolution Resource Principles ===\n")

    # Sample request mentions processing and storage across the entire dataset
    sample_request = "Process and Store the NeuralNetwork across entire dataset with hyperthreading in memory"
    result = system.process_request(sample_request)

    printc(f"Request: {sample_request}")
    printc(f"Status: {result['status']}")

    if result['status'] == 'APPROVE':
        printc(f"Identified words: {result['identified_words']}")
        printc(f"Compact representation: {result['compact_representation']['mathematical_expression']}")
        printc(f"Logic circuit: {result['logic_circuit']['name']}")
        printc(f"Operations: {result['logic_circuit']['operations']}")
        printc("Execution plan (computer axis):")
        ep = result["execution_plan"]
        printc(f"  Enabled: {ep['hyperthreading']}, Cores: {ep['cores']}, Threads/Core: {ep['threads_per_core']}, Total threads: {ep['total_threads']}")
        for tid, ops in ep["assignment"].items():
            printc(f"  {tid}: {ops}")
        printc("Time axis plan (timeline excerpts):")
        tp = result["time_axis_plan"]
        printc(f"  Timeslice: {tp['timeslice_ms']}ms, Dataset: {tp['dataset_size']} items, Chunk: {tp['chunk_size']}")
        # Show first 2 entries per thread
        for tid, segments in tp["timeline"].items():
            printc(f"  {tid}: {segments[:2]} ...")

    printc("\n=== Category Export Example ===")
    categories = system.export_categories()
    for category_name, category_data in list(categories.items())[:2]:  # Show first 2 categories
        printc(f"\n{category_name.upper()}:")
        for word, mapping in list(category_data['compact_mappings'].items())[:3]:  # Show first 3 words
            printc(f"  {word} -> {mapping['label']} (sub: {mapping['sub_words']}, ratio: {mapping['ratio']})")


if __name__ == "__main__":
    main()
