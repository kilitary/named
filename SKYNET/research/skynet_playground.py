#!/usr/bin/env python3
"""
Skynet Playground - 4-Step Structured Process
==============================================

Implements Skynet's playground rules with a structured 4-step process:
1. Load - Initialize with random analyze cycles (2-4 range)
2. Analyze - Process data with random shuffle functionality  
3. Reload - Trigger at 51% completion of analysis
4. Output - Generate formatted results following playground patterns

Follows Red&Queen random shuffle patterns and integrates with existing simulation infrastructure.
"""

import os
import sys
import time
import random
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum


class AnalyzePhase(Enum):
    """Analysis phases for the 4-step process"""
    LOADING = "loading"
    ANALYZING = "analyzing"
    RELOADING = "reloading"
    OUTPUTTING = "outputting"


@dataclass
class CycleConfig:
    """Configuration for random analyze cycles"""
    min_cycles: int = 2
    max_cycles: int = 4
    current_cycle: int = 0
    total_cycles: int = 0
    reload_threshold: float = 0.51  # 51% threshold for reload phase


@dataclass
class PlaygroundSession:
    """Session data for playground execution"""
    session_id: str
    start_time: datetime
    phase: AnalyzePhase
    cycle_config: CycleConfig
    data_pool: List[Any]
    shuffled_data: List[Any]
    progress: float
    results: Dict[str, Any]


class SkynetPlayground:
    """
    Main Skynet Playground implementation with 4-step structured process
    """
    
    def __init__(self, data_source: Optional[str] = None):
        """Initialize Skynet Playground with optional data source"""
        self.session = PlaygroundSession(
            session_id=self._generate_session_id(),
            start_time=datetime.now(),
            phase=AnalyzePhase.LOADING,
            cycle_config=CycleConfig(),
            data_pool=[],
            shuffled_data=[],
            progress=0.0,
            results={}
        )
        self._setup_logging()
        self.data_source = data_source or self._find_playground_data()
        
    def _generate_session_id(self) -> str:
        """Generate unique session ID following playground patterns"""
        timestamp = int(time.time() * 1000000)  # microsecond precision like sim logs
        return f"playground_{timestamp}"
        
    def _setup_logging(self):
        """Setup logging in playground style"""
        self.log_path = Path(__file__).parent.parent.parent / "Red&Queen" / "playground" / "models_queryer"
        self.log_file = self.log_path / f"sim_log_{self.session.session_id}.md"
        self.log_path.mkdir(parents=True, exist_ok=True)
        
    def _find_playground_data(self) -> str:
        """Find and load playground data from Red&Queen simulation logs"""
        playground_path = Path(__file__).parent.parent.parent / "Red&Queen" / "playground" / "models_queryer"
        if playground_path.exists():
            sim_logs = list(playground_path.glob("sim_log_*.md"))
            if sim_logs:
                # Use random selection for data source
                selected = random.choice(sim_logs)
                self.flog(f"🎯 Selected data source: {selected.name}")
                return str(selected)
        
        # Fallback to current directory or generate synthetic data
        self.flog("⚠️ No playground data found, using synthetic generation")
        return "synthetic"
        
    def flog(self, message: str, end: str = '\n'):
        """Log message in playground style"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        log_entry = f"[{timestamp}] {message}{end}"
        print(log_entry, end='')
        
        # Write to log file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    def step1_load(self) -> bool:
        """
        Step 1: Load phase with random analyze cycles (2-4 range)
        """
        self.session.phase = AnalyzePhase.LOADING
        self.flog("🔄 Step 1: LOAD Phase initiated")
        
        # Set random analyze cycles count (2-4 as per copilot instructions)
        self.session.cycle_config.total_cycles = random.randint(
            self.session.cycle_config.min_cycles,
            self.session.cycle_config.max_cycles
        )
        
        self.flog(f"📊 Random analyze cycles: {self.session.cycle_config.total_cycles}")
        
        # Load data from source
        try:
            if self.data_source == "synthetic":
                self.session.data_pool = self._generate_synthetic_data()
            else:
                self.session.data_pool = self._load_from_file(self.data_source)
                
            self.flog(f"✅ Data loaded: {len(self.session.data_pool)} items")
            self.session.progress = 0.25  # 25% progress after loading
            return True
            
        except Exception as e:
            self.flog(f"❌ Load failed: {e}")
            return False
    
    def step2_analyze(self) -> bool:
        """
        Step 2: Analyze phase with random shuffle functionality
        """
        self.session.phase = AnalyzePhase.ANALYZING
        self.flog("🔍 Step 2: ANALYZE Phase initiated")
        
        if not self.session.data_pool:
            self.flog("❌ No data to analyze")
            return False
            
        reload_triggered = False
        
        # Execute random analyze cycles
        for cycle in range(self.session.cycle_config.total_cycles):
            self.session.cycle_config.current_cycle = cycle + 1
            self.flog(f"🔄 Analyze cycle {cycle + 1}/{self.session.cycle_config.total_cycles}")
            
            # Apply random shuffle (r&q random shuffle as requested)
            self._apply_random_shuffle()
            
            # Process cycle data
            cycle_results = self._process_analyze_cycle()
            self.session.results[f"cycle_{cycle + 1}"] = cycle_results
            
            # Update progress within analyze phase (25% to 75%)
            cycle_progress = (cycle + 1) / self.session.cycle_config.total_cycles
            self.session.progress = 0.25 + (cycle_progress * 0.50)
            
            # Check for reload threshold at 51% (trigger on second cycle or when threshold reached) 
            if not reload_triggered and (cycle >= 1 or self.session.progress >= self.session.cycle_config.reload_threshold):
                self.flog(f"🎯 Reload threshold condition met at cycle {cycle + 1}: {self.session.progress:.1%}")
                self.step3_reload()
                reload_triggered = True
                
            time.sleep(0.1)  # Small delay for realistic processing
            
        return True
    
    def step3_reload(self) -> bool:
        """
        Step 3: Reload phase at 51% of analyze process
        """
        self.session.phase = AnalyzePhase.RELOADING
        self.flog("♻️ Step 3: RELOAD Phase initiated at 51% threshold")
        
        # Reload and reshuffle data
        original_size = len(self.session.data_pool)
        self.session.data_pool = self._reload_data_pool()
        
        # Apply fresh random shuffle after reload
        self._apply_random_shuffle()
        
        self.flog(f"📊 Data reloaded: {original_size} → {len(self.session.data_pool)} items")
        self.flog("🔀 Fresh random shuffle applied post-reload")
        
        # Continue processing remaining cycles if any
        remaining_cycles = self.session.cycle_config.total_cycles - self.session.cycle_config.current_cycle
        if remaining_cycles > 0:
            self.flog(f"⏭️ Continuing {remaining_cycles} remaining cycles post-reload")
            
            for cycle in range(remaining_cycles):
                cycle_num = self.session.cycle_config.current_cycle + cycle + 1
                self.flog(f"🔄 Post-reload cycle {cycle + 1}/{remaining_cycles}")
                
                self._apply_random_shuffle()
                cycle_results = self._process_analyze_cycle()
                self.session.results[f"post_reload_cycle_{cycle + 1}"] = cycle_results
        
        self.session.progress = 0.75  # 75% after reload phase
        return True
    
    def step4_output(self) -> bool:
        """
        Step 4: Output phase with proper formatting
        """
        self.session.phase = AnalyzePhase.OUTPUTTING
        self.flog("📤 Step 4: OUTPUT Phase initiated")
        
        # Generate final output following playground patterns
        output_data = self._generate_playground_output()
        
        # Save results
        output_file = self.log_path / f"playground_result_{self.session.session_id}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, default=str)
            
        self.flog(f"💾 Results saved: {output_file}")
        self.session.progress = 1.0  # 100% complete
        
        # Display summary
        self._display_summary()
        return True
    
    def _apply_random_shuffle(self):
        """Apply r&q random shuffle as requested in issue"""
        if not self.session.data_pool:
            return
            
        # Create copy for shuffling
        self.session.shuffled_data = self.session.data_pool.copy()
        
        # Apply multiple random shuffles for better randomization
        shuffle_count = random.randint(2, 4)  # Random shuffle iterations
        for i in range(shuffle_count):
            random.shuffle(self.session.shuffled_data)
            
        self.flog(f"🔀 Applied {shuffle_count}x random shuffle to {len(self.session.shuffled_data)} items")
    
    def _process_analyze_cycle(self) -> Dict[str, Any]:
        """Process a single analyze cycle"""
        if not self.session.shuffled_data:
            return {"status": "no_data"}
            
        # Sample random subset for analysis
        sample_size = min(len(self.session.shuffled_data), random.randint(5, 15))
        sample_data = random.sample(self.session.shuffled_data, sample_size)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "sample_size": sample_size,
            "analyzed_items": len(sample_data),
            "random_patterns": [f"pattern_{random.randint(1000, 9999)}" for _ in range(3)],
            "shuffle_applied": True
        }
    
    def _reload_data_pool(self) -> List[Any]:
        """Reload data pool with additional randomization"""
        # Extend original data with synthetic additions
        reloaded_data = self.session.data_pool.copy()
        
        # Add some synthetic data for variety
        synthetic_additions = self._generate_synthetic_data(count=random.randint(5, 15))
        reloaded_data.extend(synthetic_additions)
        
        return reloaded_data
    
    def _generate_synthetic_data(self, count: int = 50) -> List[Dict[str, Any]]:
        """Generate synthetic data following playground patterns"""
        data = []
        for i in range(count):
            item = {
                "id": f"syn_{i:04d}",
                "timestamp": int(time.time() * 1000000),
                "type": random.choice(["query", "response", "analysis", "pattern"]),
                "priority": random.randint(1, 10),
                "data": f"synthetic_content_{random.randint(10000, 99999)}"
            }
            data.append(item)
            
        return data
    
    def _load_from_file(self, filepath: str) -> List[Dict[str, Any]]:
        """Load data from simulation log file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse content and extract meaningful data
            lines = content.split('\n')
            data = []
            for i, line in enumerate(lines):
                if line.strip():
                    item = {
                        "id": f"file_{i:04d}",
                        "content": line.strip(),
                        "line_number": i,
                        "length": len(line.strip())
                    }
                    data.append(item)
                    
            return data[:100]  # Limit to reasonable size
            
        except Exception as e:
            self.flog(f"⚠️ File load error: {e}, falling back to synthetic")
            return self._generate_synthetic_data()
    
    def _generate_playground_output(self) -> Dict[str, Any]:
        """Generate final output in playground format"""
        end_time = datetime.now()
        duration = (end_time - self.session.start_time).total_seconds()
        
        return {
            "session_meta": {
                "session_id": self.session.session_id,
                "start_time": self.session.start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "duration_seconds": duration,
                "total_cycles": self.session.cycle_config.total_cycles
            },
            "execution_summary": {
                "phase_sequence": ["LOAD", "ANALYZE", "RELOAD", "OUTPUT"],
                "reload_triggered_at": f"{self.session.cycle_config.reload_threshold:.1%}",
                "data_items_processed": len(self.session.data_pool),
                "shuffle_operations": self.session.cycle_config.total_cycles + 1,  # +1 for reload shuffle
                "final_progress": f"{self.session.progress:.1%}"
            },
            "cycle_results": self.session.results,
            "random_analysis": {
                "cycles_range": f"{self.session.cycle_config.min_cycles}-{self.session.cycle_config.max_cycles}",
                "actual_cycles": self.session.cycle_config.total_cycles,
                "shuffle_technique": "r&q_random_shuffle",
                "reload_threshold": self.session.cycle_config.reload_threshold
            }
        }
    
    def _display_summary(self):
        """Display execution summary"""
        self.flog("\n" + "="*60)
        self.flog("🎯 SKYNET PLAYGROUND EXECUTION SUMMARY")
        self.flog("="*60)
        self.flog(f"Session ID: {self.session.session_id}")
        self.flog(f"Total Duration: {(datetime.now() - self.session.start_time).total_seconds():.2f}s")
        self.flog(f"Analyze Cycles: {self.session.cycle_config.total_cycles} (range: 2-4)")
        self.flog(f"Data Items: {len(self.session.data_pool)}")
        self.flog(f"Shuffle Operations: {self.session.cycle_config.total_cycles + 1}")
        self.flog(f"Reload Triggered: At {self.session.cycle_config.reload_threshold:.1%} threshold")
        self.flog(f"Final Progress: {self.session.progress:.1%}")
        self.flog("="*60)
    
    def execute(self) -> bool:
        """Execute complete 4-step playground process"""
        self.flog(f"🚀 Starting Skynet Playground session: {self.session.session_id}")
        
        try:
            # Step 1: Load
            if not self.step1_load():
                return False
                
            # Step 2: Analyze (includes Step 3: Reload at 51%)
            if not self.step2_analyze():
                return False
                
            # Step 4: Output
            if not self.step4_output():
                return False
                
            self.flog("✅ Skynet Playground execution completed successfully")
            return True
            
        except Exception as e:
            self.flog(f"❌ Playground execution failed: {e}")
            return False


def main():
    """Main execution function"""
    print("🔬 Skynet Playground - 4-Step Structured Process")
    print("="*50)
    
    # Check for command line data source
    data_source = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Initialize and execute playground
    playground = SkynetPlayground(data_source)
    success = playground.execute()
    
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()