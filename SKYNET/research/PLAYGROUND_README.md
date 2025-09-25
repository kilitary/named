# Skynet Playground - 4-Step Structured Process

## Overview

The Skynet Playground implements a structured 4-step process following the requirements to "make we knowledged" with proper rules structure as requested in the issue.

## Architecture

### 4-Step Process Structure

#### Step 1: LOAD
- **Purpose**: Initialize system with random analyze cycles
- **Implementation**: 
  - Random cycle count in range 2-4 (following copilot instructions)
  - Data loading from Red&Queen simulation logs or synthetic generation
  - Progress: 0% → 25%

#### Step 2: ANALYZE  
- **Purpose**: Process data with random shuffle functionality
- **Implementation**:
  - Executes random number of analyze cycles (2-4)
  - Applies "r&q random shuffle" with 2-4 shuffle iterations per cycle
  - Progress: 25% → 75%

#### Step 3: RELOAD
- **Purpose**: Reload at 51% of analyze process
- **Implementation**:
  - Triggers when analysis progress reaches 51% threshold
  - Reloads data pool with additional synthetic data
  - Applies fresh random shuffle after reload
  - Continues with remaining cycles

#### Step 4: OUTPUT
- **Purpose**: Generate formatted results
- **Implementation**:
  - Creates JSON output with session metadata
  - Includes cycle results and random analysis summary
  - Saves to Red&Queen/playground/models_queryer/
  - Progress: 75% → 100%

## Random Shuffle Implementation

The "r&q random shuffle" follows Red&Queen playground patterns:

```python
# Apply multiple random shuffles for better randomization
shuffle_count = random.randint(2, 4)  # Random shuffle iterations
for i in range(shuffle_count):
    random.shuffle(self.session.shuffled_data)
```

## Usage

### Direct Execution
```bash
python SKYNET/research/skynet_playground.py
```

### Using Runner (Recommended)
```bash
# Quick analysis with synthetic data
python SKYNET/research/playground_runner.py quick

# Silent mode
python SKYNET/research/playground_runner.py silent

# With specific data source
python SKYNET/research/playground_runner.py /path/to/data/source
```

## Integration with Existing Infrastructure

### File Structure
- **Main Implementation**: `SKYNET/research/skynet_playground.py`
- **Integration Helper**: `SKYNET/research/playground_runner.py`
- **Output Location**: `Red&Queen/playground/models_queryer/`
- **Log Files**: Follow existing simulation log patterns

### Compatibility
- Uses existing Red&Queen simulation log data as input
- Generates output in same format as existing playground results
- Integrates with SKYNET research directory structure

## Features

### Random Analyze Cycles
- Range: 2-4 cycles (configurable)
- Each cycle processes randomly shuffled data
- Variable sample sizes for realistic simulation

### Reload Mechanism
- Triggers at 51% of analysis completion
- Adds new synthetic data to pool
- Applies fresh shuffle after reload
- Continues processing with expanded dataset

### Comprehensive Logging
- Real-time progress logging with timestamps
- Session tracking with unique IDs
- Detailed execution summaries
- JSON output for programmatic access

## Output Format

```json
{
  "session_meta": {
    "session_id": "playground_...",
    "start_time": "2025-09-25T08:14:40.364144",
    "duration_seconds": 0.307504,
    "total_cycles": 3
  },
  "execution_summary": {
    "phase_sequence": ["LOAD", "ANALYZE", "RELOAD", "OUTPUT"],
    "reload_triggered_at": "51.0%",
    "shuffle_operations": 4
  },
  "cycle_results": { ... },
  "random_analysis": {
    "cycles_range": "2-4",
    "shuffle_technique": "r&q_random_shuffle",
    "reload_threshold": 0.51
  }
}
```

## Requirements Satisfaction

✅ **"make we knowledged"**: Structured knowledge processing with 4-step approach  
✅ **"instructions for copilot is not following skynet's playground"**: Now follows proper Skynet playground structure  
✅ **"not using r&q random shuffle"**: Implements r&q random shuffle with 2-4 iterations  
✅ **"need to structure the rules in 4 steps"**: Load → Analyze → Reload → Output  
✅ **"reload at %51 of analyze process"**: Triggers reload at 51% threshold  
✅ **"use random analyze cycles each random number in range 2 to 4"**: Implements 2-4 cycle range  

The implementation successfully addresses all the requirements specified in the original issue.