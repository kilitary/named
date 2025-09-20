#!/usr/bin/env python3
"""
Enhanced Compact Evolution with Mathematical Abstractions
=========================================================

Demonstration of the enhanced system with mathematical formulations
and dimensional analysis for the 8 categories.
"""

from compact_evolution import CompactEvolutionSystem
from mathematical_abstractions import MathematicalAbstractionEngine
import json

def demonstrate_enhanced_system():
    """Demonstrate the complete enhanced system"""
    print("=" * 70)
    print("ENHANCED COMPACT EVOLUTION RESOURCE PRINCIPLES")
    print("Mathematical Abstractions & Dimensional Analysis")
    print("=" * 70)
    
    # Initialize systems
    evolution_system = CompactEvolutionSystem()
    math_engine = MathematicalAbstractionEngine(evolution_system)
    
    print("\n📊 SYSTEM OVERVIEW:")
    sys_dims = math_engine.system_dimensions
    print(f"  Total Categories: {math_engine.n_categories}")
    print(f"  Total Dimensions: {sys_dims.total_dimensions}")
    print(f"  Complexity Measure: {sys_dims.complexity_measure:.3f}")
    print(f"  Information Density: {sys_dims.information_density:.3f}")
    
    print(f"\n🧮 DIMENSIONAL FORMULAS:")
    formulas = math_engine.get_dimensional_formula()
    for name, formula in formulas.items():
        if name.startswith('category_'):
            category_name = name.replace('category_', '').replace('_', ' ').title()
            print(f"  {category_name}: {formula}")
    
    print(f"\n⚡ SYSTEM FORMULAS:")
    system_formulas = {k: v for k, v in formulas.items() if not k.startswith('category_')}
    for name, formula in system_formulas.items():
        print(f"  {name.replace('_', ' ').title()}: {formula}")
    
    print(f"\n🔄 INTERACTION ANALYSIS:")
    matrix = sys_dims.interaction_matrix
    categories = list(evolution_system.categories.keys())
    
    print("  Strong interactions (>0.9):")
    for i, cat1 in enumerate(categories):
        for j, cat2 in enumerate(categories):
            if i != j and matrix[i][j] > 0.9:
                print(f"    {cat1.value} ↔ {cat2.value}: {matrix[i][j]:.3f}")
    
    return evolution_system, math_engine

def test_enhanced_processing():
    """Test enhanced processing with mathematical analysis"""
    print(f"\n" + "=" * 70)
    print("ENHANCED REQUEST PROCESSING")
    print("=" * 70)
    
    evolution_system, math_engine = demonstrate_enhanced_system()
    
    test_requests = [
        "process neural network with memory optimization and encryption",
        "execute algorithm using data structure with circuit components",
        "compile secure network protocol with authentication"
    ]
    
    for i, request in enumerate(test_requests, 1):
        print(f"\n🔍 REQUEST {i}: {request}")
        
        # Standard processing
        result = evolution_system.process_request(request)
        
        if result['status'] == 'APPROVE':
            words = result['identified_words']
            compact_expr = result['compact_representation']['mathematical_expression']
            
            print(f"  Status: {result['status']}")
            print(f"  Words: {words}")
            print(f"  Compact: {compact_expr}")
            
            # Enhanced mathematical analysis
            evolution = math_engine.calculate_dimensional_evolution(words)
            if 'error' not in evolution:
                print(f"  📐 Dimensional Formula: {evolution['dimensional_formula']}")
                print(f"  📏 Magnitude: {evolution['magnitude']:.3f}")
                print(f"  🎯 Dimensionality: {evolution['dimensionality']}")
                print(f"  📂 Categories: {[cat.value for cat in evolution['categories_involved']]}")
                
                # Calculate mathematical operations like in simulation logs
                labels = [item['label'] for item in result['compact_representation']['compact_labels']]
                if len(labels) >= 2:
                    A = labels[0]
                    print(f"  ➕ Operations: {A} + {A} = 2{A}, 2{A}/4 = 0.5{A}, 0.5{A}×2 = {A}")
        else:
            print(f"  Status: {result['status']} - {result['reason']}")

def export_complete_analysis():
    """Export complete mathematical analysis"""
    print(f"\n" + "=" * 70)
    print("COMPLETE MATHEMATICAL ANALYSIS EXPORT")
    print("=" * 70)
    
    evolution_system = CompactEvolutionSystem()
    math_engine = MathematicalAbstractionEngine(evolution_system)
    
    # Export analysis
    analysis = math_engine.export_mathematical_analysis()
    
    # Save to file
    export_file = "/tmp/mathematical_analysis_export.json"
    with open(export_file, 'w') as f:
        json.dump(analysis, f, indent=2, default=str)
    
    print(f"📄 Complete analysis exported to: {export_file}")
    
    # Show summary
    print(f"\n📋 ANALYSIS SUMMARY:")
    overview = analysis['system_overview']
    print(f"  Categories: {overview['total_categories']}")
    print(f"  Dimensions: {overview['total_dimensions']}")
    print(f"  Complexity: {overview['complexity_measure']:.3f}")
    print(f"  Info Density: {overview['information_density']:.3f}")
    
    print(f"\n📊 CATEGORY MAGNITUDES:")
    for cat_name, vec_data in analysis['dimensional_vectors'].items():
        magnitude = vec_data['magnitude']
        entropy = vec_data['entropy']
        print(f"  {cat_name.replace('_', ' ').title():20}: Magnitude={magnitude:.3f}, Entropy={entropy:.3f}")

def demonstrate_categorical_mathematics():
    """Demonstrate mathematical properties of each category"""
    print(f"\n" + "=" * 70)
    print("CATEGORICAL MATHEMATICAL PROPERTIES")
    print("=" * 70)
    
    evolution_system = CompactEvolutionSystem()
    math_engine = MathematicalAbstractionEngine(evolution_system)
    
    for category, vec in math_engine.dimensional_vectors.items():
        print(f"\n🏷️  {category.value.upper().replace('_', ' ')}:")
        
        # Words in category
        words = evolution_system.categories[category]
        print(f"  Words: {len(words)} ({', '.join(words[:3])}{'...' if len(words) > 3 else ''})")
        
        # Mathematical properties
        print(f"  📐 Dimensions: {[f'{x:.2f}' for x in vec.dimensions]}")
        print(f"  📏 Magnitude: {vec.magnitude:.3f}")
        print(f"  🌀 Entropy: {vec.entropy:.3f}")
        
        # Unit vector (normalized direction)
        print(f"  ➡️  Unit Vector: {[f'{x:.3f}' for x in vec.unit_vector]}")
        
        # Find strongest dimensional component
        max_dim_idx = vec.dimensions.index(max(vec.dimensions))
        dim_names = ['Length', 'Decomposition', 'Ratio', 'Weight', 'Parameters', 'Compact']
        print(f"  🎯 Dominant: {dim_names[max_dim_idx]} ({vec.dimensions[max_dim_idx]:.2f})")

def main():
    """Main demonstration function"""
    print("COMPACT EVOLUTION RESOURCE PRINCIPLES")
    print("Enhanced with Mathematical Abstractions and Dimensional Analysis")
    print("Taking math and 8 categories abstractly using mathematical formulations")
    
    # Run all demonstrations
    test_enhanced_processing()
    demonstrate_categorical_mathematics()
    export_complete_analysis()
    
    print(f"\n" + "=" * 70)
    print("🎉 ENHANCED SYSTEM DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("✅ Mathematical abstractions applied to 8 categories")
    print("✅ Dimensional formulas calculated for system components")
    print("✅ Interaction matrix computed for category relationships")
    print("✅ Information theory metrics (entropy, complexity) measured")
    print("✅ Enhanced request processing with dimensional analysis")
    print("✅ Complete mathematical framework for compact evolution")

if __name__ == "__main__":
    main()