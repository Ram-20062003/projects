# Create a detailed breakdown of the bottom-up implementation

bottom_up_explanation = """
# Bottom-Up (Neural Network) Implementation - Detailed Breakdown

## 1. DATA REPRESENTATION

### Shape Features (Input Layer - 8 Nodes)
Each shape is converted to numerical features that represent its characteristics:

```javascript
// Example: Square features
square_features = [
    0.9,  // Corner Count (high = many corners)
    0.1,  // Curve Presence (low = no curves) 
    0.9,  // Side Count (high = 4 sides)
    0.9,  // Side Equality (high = equal sides)
    0.2,  // Angle Measure (normalized)
    0.1,  // Symmetry Type (encoded numerically)
    0.9,  // Area Ratio (shape-specific)
    0.8   // Perimeter Ratio (shape-specific)
];

// Example: Circle features  
circle_features = [
    0.1,  // Corner Count (low = no corners)
    0.9,  // Curve Presence (high = curved)
    0.2,  // Side Count (low = no distinct sides)
    0.1,  // Side Equality (not applicable)
    0.8,  // Angle Measure (continuous)
    0.9,  // Symmetry Type (radial)
    0.1,  // Area Ratio
    0.2   // Perimeter Ratio
];
```

## 2. NETWORK SIMULATION PROCESS

### Step 1: Input to Hidden Layer Processing
```javascript
function processInputToHidden(inputFeatures) {
    let hiddenActivations = [];
    
    // For each hidden node (6 nodes total)
    for (let hiddenNode = 0; hiddenNode < 6; hiddenNode++) {
        let weightedSum = 0;
        
        // Process all 8 input features
        for (let inputNode = 0; inputNode < 8; inputNode++) {
            // Simulate learned weights (normally trained through backpropagation)
            let weight = getSimulatedWeight(inputNode, hiddenNode);
            
            // Multiply input by weight and add to sum
            weightedSum += inputFeatures[inputNode] * weight;
        }
        
        // Add bias (normally learned parameter)
        let bias = getSimulatedBias(hiddenNode);
        weightedSum += bias;
        
        // Apply sigmoid activation function
        // This squashes output to 0-1 range
        hiddenActivations[hiddenNode] = sigmoid(weightedSum);
    }
    
    return hiddenActivations;
}

// Sigmoid activation function
function sigmoid(x) {
    return 1 / (1 + Math.exp(-x));
}
```

### Step 2: Hidden to Output Layer Processing
```javascript
function processHiddenToOutput(hiddenActivations) {
    let outputActivations = []; // 4 outputs for 4 shape classes
    
    // For each output class (Circle, Square, Triangle, Rectangle)
    for (let outputNode = 0; outputNode < 4; outputNode++) {
        let weightedSum = 0;
        
        // Process all 6 hidden activations
        for (let hiddenNode = 0; hiddenNode < 6; hiddenNode++) {
            let weight = getSimulatedWeight(hiddenNode, outputNode);
            weightedSum += hiddenActivations[hiddenNode] * weight;
        }
        
        // Add output bias
        let bias = getSimulatedBias(outputNode);
        weightedSum += bias;
        
        // Apply sigmoid activation
        outputActivations[outputNode] = sigmoid(weightedSum);
    }
    
    return outputActivations;
}
```

## 3. SIMULATION OF LEARNING (What Real Networks Do)

### Weight Simulation
```javascript
// In real networks, weights are learned through training
// For demo, we simulate reasonable weights based on shape characteristics
function getSimulatedWeight(fromNode, toNode) {
    // Create deterministic but varied weights for demo purposes
    let seed = (fromNode * 7 + toNode * 13) % 100;
    
    // Normalize to reasonable weight range (-1 to 1)
    return (seed / 50) - 1;
}

// Alternative: Use feature-aware weights for better simulation
function getFeatureAwareWeight(featureIndex, shapeClass) {
    let weights = {
        'circle': [0.1, 0.9, 0.1, 0.1, 0.3, 0.8, 0.2, 0.1],    // Low corners, high curves
        'square': [0.9, 0.1, 0.9, 0.9, 0.8, 0.2, 0.8, 0.9],    // High corners, low curves
        'triangle': [0.7, 0.1, 0.7, 0.6, 0.6, 0.3, 0.5, 0.4],  // Medium values
        'rectangle': [0.8, 0.1, 0.8, 0.3, 0.7, 0.2, 0.6, 0.2]  // 4 corners, unequal sides
    };
    
    return weights[shapeClass][featureIndex];
}
```

## 4. VISUAL ANIMATION IMPLEMENTATION

### Node Activation Animation
```javascript
function animateNeuralNetwork(inputFeatures) {
    // Step 1: Light up input nodes based on feature values
    animateInputNodes(inputFeatures);
    
    // Step 2: Show processing from input to hidden
    setTimeout(() => {
        let hiddenActivations = processInputToHidden(inputFeatures);
        animateHiddenNodes(hiddenActivations);
    }, 500);
    
    // Step 3: Show processing from hidden to output
    setTimeout(() => {
        let outputActivations = processHiddenToOutput(hiddenActivations);
        animateOutputNodes(outputActivations);
        showFinalPrediction(outputActivations);
    }, 1000);
}

function animateInputNodes(features) {
    features.forEach((value, index) => {
        let node = document.getElementById(`input-node-${index}`);
        
        // Set brightness based on activation level
        let brightness = Math.round(value * 100);
        node.style.backgroundColor = `hsl(200, 70%, ${brightness}%)`;
        
        // Add pulsing animation
        node.classList.add('active-node');
    });
}
```

### Connection Weight Visualization
```javascript
function animateConnections(fromLayer, toLayer, weights) {
    fromLayer.forEach((fromNode, fromIndex) => {
        toLayer.forEach((toNode, toIndex) => {
            let connectionElement = document.getElementById(
                `connection-${fromIndex}-${toIndex}`
            );
            
            // Make connection thickness proportional to weight strength
            let weight = weights[fromIndex][toIndex];
            let thickness = Math.abs(weight) * 3; // Scale for visibility
            
            connectionElement.style.strokeWidth = `${thickness}px`;
            
            // Color based on weight sign (positive/negative)
            connectionElement.style.stroke = weight > 0 ? '#4CAF50' : '#F44336';
            
            // Animate data flow
            connectionElement.classList.add('data-flow');
        });
    });
}
```

## 5. PREDICTION AND CONFIDENCE

### Final Classification
```javascript
function makeNetworkPrediction(outputActivations) {
    let shapeClasses = ['circle', 'square', 'triangle', 'rectangle'];
    
    // Find the output with highest activation
    let maxActivation = Math.max(...outputActivations);
    let predictedClassIndex = outputActivations.indexOf(maxActivation);
    let predictedShape = shapeClasses[predictedClassIndex];
    
    // Confidence is the activation strength (0-1, convert to percentage)
    let confidence = Math.round(maxActivation * 100);
    
    return {
        prediction: predictedShape,
        confidence: confidence,
        allActivations: outputActivations.map(act => Math.round(act * 100))
    };
}
```

## 6. KEY DIFFERENCES FROM TOP-DOWN

### Data Processing
- **Top-Down**: Discrete rule matching (corners: 4 ✓ or ✗)
- **Bottom-Up**: Continuous numerical processing (0.9 * weight + bias)

### Decision Logic  
- **Top-Down**: IF corners==4 AND angles==90 THEN square
- **Bottom-Up**: sigmoid(Σ(features × weights) + bias) for each class

### Learning Capability
- **Top-Down**: Rules are fixed, programmed by experts
- **Bottom-Up**: Weights learned from training data (simulated in demo)

### Explainability
- **Top-Down**: "Square because it has 4 equal sides and 90° angles"
- **Bottom-Up**: "Network activation of 0.89 for square class" (no deeper explanation)

This implementation demonstrates how connectionist AI processes information through 
mathematical transformations rather than logical rules, showing the fundamental 
difference in approaches to artificial intelligence.
"""

print(bottom_up_explanation)