#!/usr/bin/env python3
"""
Red&Queen Random Utilities
===========================

Repository-wide R&Q random system implementation following the corrected logic:
1. Get analog or other really random byte at start and seed random
2. Get 1-byte random value "num_skip"  
3. "num_skip" random times get random value in range 1 to 10
   if acquired random value is 5, go to next step, else discard value and continue loop
4. Make a func for getting random value for entire repository using steps 2-3

This module provides the corrected R&Q random system for the entire repository.
"""

import random
import time
import os
from typing import List, Any


class RQRandomSystem:
    """
    Red&Queen Random System Implementation
    
    Implements proper R&Q random shuffle system with true random seeding
    and skip-based random value generation as specified.
    """
    
    def __init__(self):
        """Initialize R&Q Random System with true random seed"""
        self._initialize_true_random_seed()
        self.operation_count = 0
        
    def _initialize_true_random_seed(self):
        """
        Step 1: Get analog/truly random byte from OS and seed random
        Uses OS entropy pool for true randomness
        """
        try:
            # Get truly random bytes from OS entropy pool (/dev/urandom on Unix)
            random_bytes = os.urandom(8)  # 8 bytes for strong seed
            seed_value = int.from_bytes(random_bytes, byteorder='big')
            random.seed(seed_value)
            
            self.seed_info = {
                "type": "OS_ENTROPY",
                "seed": seed_value & 0xFFFFFFFF,  # Show lower 32 bits
                "full_seed": seed_value,
                "entropy_bytes": random_bytes.hex().upper()
            }
            
            print(f"🎲 R&Q Random System initialized")
            print(f"   Entropy source: OS urandom")
            print(f"   Seed: {self.seed_info['seed']:08X}")
            print(f"   Full entropy: {self.seed_info['entropy_bytes'][:20]}...")
            
        except Exception as e:
            # Fallback to high-precision time-based seed if OS entropy fails
            fallback_seed = int(time.time() * 1000000) % (2**32)
            random.seed(fallback_seed)
            
            self.seed_info = {
                "type": "TIME_FALLBACK", 
                "seed": fallback_seed,
                "error": str(e)
            }
            
            print(f"⚠️  R&Q Random System fallback initialization")
            print(f"   Reason: {e}")
            print(f"   Time-based seed: {fallback_seed:08X}")
    
    def get_rq_random_value(self, min_val: int = 0, max_val: int = 255) -> int:
        """
        Get R&Q random value using the specified algorithm:
        
        Steps 2-3:
        2. Get 1-byte random value "num_skip"
        3. "num_skip" random times get random value in range 1 to 10
           if acquired random value is 5, go to next step, else discard and continue
        
        Args:
            min_val: Minimum value for final random result
            max_val: Maximum value for final random result
            
        Returns:
            Random value in range [min_val, max_val] using R&Q algorithm
        """
        self.operation_count += 1
        
        # Step 2: Get 1-byte random value "num_skip"
        num_skip = random.randint(0, 255)
        
        # Step 3: Skip process - get random values until we get 5
        skip_count = 0
        discarded_values = []
        
        while skip_count < num_skip:
            test_value = random.randint(1, 10)
            if test_value == 5:
                # Got 5, exit skip loop
                break
            else:
                # Discard value and continue loop
                discarded_values.append(test_value)
                skip_count += 1
        
        # Now get the actual random value in the requested range
        final_value = random.randint(min_val, max_val)
        
        # Debug info for first few operations
        if self.operation_count <= 3:
            print(f"   R&Q Random Op #{self.operation_count}: num_skip={num_skip}, "
                  f"discarded={len(discarded_values)}, final={final_value}")
        
        return final_value
    
    def rq_shuffle(self, data_list: List[Any]) -> None:
        """
        R&Q random shuffle using the proper random system
        
        Implements Fisher-Yates shuffle using R&Q random values
        """
        if len(data_list) <= 1:
            return
            
        # Fisher-Yates shuffle with R&Q random
        for i in range(len(data_list) - 1, 0, -1):
            j = self.get_rq_random_value(0, i)
            data_list[i], data_list[j] = data_list[j], data_list[i]
    
    def get_rq_random_int(self, min_val: int, max_val: int) -> int:
        """Get R&Q random integer in specified range"""
        return self.get_rq_random_value(min_val, max_val)
    
    def get_rq_random_hex_check(self, length: int = 10) -> str:
        """
        Generate R&Q random hex check like simulation logs
        
        Args:
            length: Number of hex bytes to generate
            
        Returns:
            Space-separated hex string like "7A AC 0D 1D DA 61 E6 0E B5 AE"
        """
        hex_values = []
        for _ in range(length):
            hex_val = self.get_rq_random_value(0, 255)
            hex_values.append(f"{hex_val:02X}")
        return ' '.join(hex_values)
    
    def get_rq_cycles(self, min_cycles: int = 2, max_cycles: int = 4) -> int:
        """Get R&Q random cycles in range (for analyze cycles)"""
        return self.get_rq_random_value(min_cycles, max_cycles)
    
    def get_system_info(self) -> dict:
        """Get R&Q random system information"""
        return {
            "seed_info": self.seed_info,
            "operations_performed": self.operation_count,
            "system_status": "ACTIVE"
        }


# Global R&Q Random System instance for repository-wide use
_global_rq_random = None

def get_rq_random() -> RQRandomSystem:
    """
    Get the global R&Q Random System instance for entire repository use
    
    This function implements step 4: "make a func for getting random value 
    for entire repository using steps 2-3"
    
    Returns:
        Global RQRandomSystem instance
    """
    global _global_rq_random
    if _global_rq_random is None:
        _global_rq_random = RQRandomSystem()
    return _global_rq_random

def rq_randint(min_val: int, max_val: int) -> int:
    """Repository-wide R&Q random integer function"""
    return get_rq_random().get_rq_random_int(min_val, max_val)

def rq_shuffle(data_list: List[Any]) -> None:
    """Repository-wide R&Q shuffle function"""
    get_rq_random().rq_shuffle(data_list)

def rq_hex_check(length: int = 10) -> str:
    """Repository-wide R&Q hex check generation"""
    return get_rq_random().get_rq_random_hex_check(length)

def rq_cycles(min_cycles: int = 2, max_cycles: int = 4) -> int:
    """Repository-wide R&Q cycles generation"""
    return get_rq_random().get_rq_cycles(min_cycles, max_cycles)

def rq_choice(choices: List[Any]) -> Any:
    """Repository-wide R&Q random choice function"""
    if not choices:
        return None
    index = get_rq_random().get_rq_random_value(0, len(choices) - 1)
    return choices[index]


def test_rq_random_system():
    """Test the R&Q random system implementation"""
    print("=" * 70)
    print("RED&QUEEN RANDOM SYSTEM TEST")
    print("Testing corrected R&Q random logic")
    print("=" * 70)
    
    rq = get_rq_random()
    
    print(f"\n📊 SYSTEM INFO:")
    info = rq.get_system_info()
    print(f"   Seed Type: {info['seed_info']['type']}")
    print(f"   Seed Value: {info['seed_info']['seed']:08X}")
    
    print(f"\n🧪 TESTING R&Q RANDOM VALUES:")
    for i in range(5):
        val = rq.get_rq_random_value(0, 100)
        print(f"   Test {i+1}: R&Q Random(0-100) = {val}")
    
    print(f"\n🔀 TESTING R&Q SHUFFLE:")
    test_data = list(range(10))
    original = test_data.copy()
    rq.rq_shuffle(test_data)
    print(f"   Original: {original}")
    print(f"   Shuffled: {test_data}")
    
    print(f"\n🎲 TESTING HEX CHECK GENERATION:")
    hex_check = rq.get_rq_random_hex_check(10)
    print(f"   R&Q Hex Check: {hex_check}")
    
    print(f"\n📈 FINAL STATS:")
    final_info = rq.get_system_info()
    print(f"   Operations: {final_info['operations_performed']}")
    print(f"   Status: {final_info['system_status']}")
    
    print(f"\n✅ R&Q RANDOM SYSTEM TEST COMPLETE")


if __name__ == "__main__":
    test_rq_random_system()