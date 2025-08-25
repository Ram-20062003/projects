# Let me create a detailed technical explanation of how both approaches work in the demo

implementation_explanation = """
# How the AI Approaches Demo Works - Technical Implementation

## Overview
The demo implements two different AI paradigms for the same shape recognition task:
1. **Top-Down (Symbolic AI)**: Rule-based reasoning with explicit logic
2. **Bottom-Up (Connectionist AI)**: Neural network pattern recognition

## 1. TOP-DOWN APPROACH IMPLEMENTATION

### Data Structure
Each shape has predefined rules stored as structured data:
```javascript
shapes = {
    square: {
        rules: {
            corners: 4,           // Must have 4 corners
            curves: 0,            // No curved edges  
            symmetry: "4-fold",   // 4-way rotational symmetry
            equal_sides: true     // All sides must be equal
        }
    },
    circle: {
        rules: {
            corners: 0,           // No corners
            curves: 1,            // Has curved edges
            symmetry: "radial",   // Radial symmetry
            equal_sides: false    // No concept of sides
        }
    }
    // ... other shapes
}
```

### Rule Evaluation Process
1. **Input**: User selects a shape (e.g., "square")
2. **Rule Matching**: System checks each rule against the selected shape's properties
3. **Step-by-step Evaluation**:
   - "Has 4 corners: ✓" (corners: 4 matches expected 4)
   - "No curved edges: ✓" (curves: 0 matches expected 0) 
   - "4-fold symmetry: ✓" (symmetry matches)
   - "All sides equal: ✓" (equal_sides: true matches)

### Confidence Calculation
```javascript
function calculateTopDownConfidence(selectedShape, targetShape) {
    const rules = shapes[targetShape].rules;
    const actualRules = shapes[selectedShape].rules;
    
    let matchCount = 0;
    let totalRules = 0;
    
    for (rule in rules) {
        totalRules++;
        if (actualRules[rule] === rules[rule]) {
            matchCount++;
        }
    }
    
    return (matchCount / totalRules) * 100; // Percentage match
}
```

### Visual Display
- Shows each rule being evaluated with checkmarks (✓) or crosses (✗)
- Displays reasoning: "Because shape has 4 corners and equal sides..."
- Confidence based on percentage of rules matched

---

## 2. BOTTOM-UP APPROACH IMPLEMENTATION

### Neural Network Structure
```javascript
networkStructure = {
    inputLayer: 8 nodes,    // Feature extraction from shape
    hiddenLayer: 6 nodes,   // Pattern processing
    outputLayer: 4 nodes    // One for each shape class
}
```

### Feature Extraction
Each shape is represented as a numerical feature vector:
```javascript
features = {
    circle:    [0.1, 0.9, 0.2, 0.1, 0.8, 0.9, 0.1, 0.2],
    square:    [0.9, 0.1, 0.9, 0.9, 0.2, 0.1, 0.9, 0.8],
    triangle:  [0.7, 0.2, 0.7, 0.6, 0.3, 0.2, 0.7, 0.5],
    rectangle: [0.8, 0.1, 0.8, 0.6, 0.2, 0.1, 0.8, 0.4]
}

// Features represent:
// [corner_count, curve_presence, side_count, side_equality, 
//  angle_measure, symmetry_type, area_ratio, perimeter_ratio]
```

### Forward Propagation Simulation
```javascript
function simulateNeuralNetwork(inputFeatures) {
    // Layer 1: Input to Hidden
    let hiddenActivations = [];
    for (let h = 0; h < hiddenNodes; h++) {
        let weightedSum = 0;
        for (let i = 0; i < inputFeatures.length; i++) {
            // Simulate random weights (in real network, these are learned)
            let weight = Math.random() * 0.5 + 0.25; 
            weightedSum += inputFeatures[i] * weight;
        }
        // Apply sigmoid activation function
        hiddenActivations[h] = 1 / (1 + Math.exp(-weightedSum));
    }
    
    // Layer 2: Hidden to Output  
    let outputActivations = [];
    for (let o = 0; o < 4; o++) { // 4 output classes
        let weightedSum = 0;
        for (let h = 0; h < hiddenActivations.length; h++) {
            let weight = Math.random() * 0.5 + 0.25;
            weightedSum += hiddenActivations[h] * weight;
        }
        outputActivations[o] = 1 / (1 + Math.exp(-weightedSum));
    }
    
    return outputActivations;
}
```

### Prediction Process
1. **Input**: Selected shape's feature vector
2. **Processing**: Features flow through network layers
3. **Activation**: Each node processes weighted inputs through sigmoid function
4. **Output**: 4 values representing confidence for each shape class
5. **Prediction**: Highest output value indicates predicted class

### Visual Animation
- Nodes light up based on activation levels
- Connections pulse to show data flow
- Progress bars show activation strength
- Network "learns" through animated weight adjustments

---

## 3. KEY IMPLEMENTATION DIFFERENCES

### Data Representation
- **Top-Down**: Explicit symbolic rules (corners: 4, curves: 0)
- **Bottom-Up**: Numerical feature vectors [0.9, 0.1, 0.9, 0.9...]

### Decision Making
- **Top-Down**: Logical rule evaluation with boolean results
- **Bottom-Up**: Mathematical transformations through weighted connections

### Confidence Calculation
- **Top-Down**: Percentage of rules matched (discrete)
- **Bottom-Up**: Network activation strength (continuous)

### Explainability
- **Top-Down**: Can show exact reasoning ("Has 4 corners: ✓")
- **Bottom-Up**: Cannot explain why (weights are abstract numbers)

---

## 4. DEMO FLOW IMPLEMENTATION

### User Interaction Sequence
1. **Shape Selection**: 
   ```javascript
   shapeButtons.forEach(button => {
       button.addEventListener('click', () => {
           selectedShape = button.dataset.shape;
           drawShapeOnCanvas(selectedShape);
           enableAnalyzeButton();
       });
   });
   ```

2. **Analysis Trigger**:
   ```javascript
   analyzeButton.addEventListener('click', () => {
       runTopDownAnalysis(selectedShape);
       runBottomUpAnalysis(selectedShape);
       showComparisonResults();
   });
   ```

3. **Parallel Execution**: Both approaches analyze the same input simultaneously

4. **Results Display**: Side-by-side comparison with explanations

### Animation System
- CSS transitions for smooth visual effects
- JavaScript timers for step-by-step rule evaluation
- Canvas animations for neural network visualization
- Progressive disclosure of results

This implementation effectively demonstrates the fundamental philosophical and technical differences between symbolic and connectionist AI approaches using the same problem domain.
"""

print(implementation_explanation)