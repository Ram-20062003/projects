# COMPARISON: TOP-DOWN vs BOTTOM-UP AI APPROACHES
import numpy as np

# Both classes from previous examples (abbreviated for slides)
class SymbolicAI:
    def __init__(self):
        self.rules = {
            'square': {'corners': 4, 'equal_sides': True, 'angles': 90},
            'circle': {'corners': 0, 'curves': True, 'symmetry': 'radial'},
            'triangle': {'corners': 3, 'angles_sum': 180}
        }
    
    def classify(self, shape_properties):
        for shape_name, rules in self.rules.items():
            matches = sum(1 for rule, expected in rules.items() 
                         if shape_properties.get(rule) == expected)
            confidence = (matches / len(rules)) * 100
            if confidence >= 75:
                return shape_name, confidence
        return "unknown", 0

class NeuralNetwork:
    def __init__(self):
        np.random.seed(42)
        self.weights_ih = np.random.randn(4, 3) * 0.5
        self.weights_ho = np.random.randn(3, 3) * 0.5
        self.bias_h = np.random.randn(3) * 0.1
        self.bias_o = np.random.randn(3) * 0.1
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def classify(self, features):
        # Forward propagation
        hidden = self.sigmoid(np.dot(features, self.weights_ih) + self.bias_h)
        output = self.sigmoid(np.dot(hidden, self.weights_ho) + self.bias_o)
        
        classes = ['square', 'circle', 'triangle']
        prediction_idx = np.argmax(output)
        confidence = output[prediction_idx] * 100
        
        return classes[prediction_idx], confidence

def compare_approaches():
    """Side-by-side comparison of both AI approaches"""
    
    # Same logical shape: Square
    symbolic_input = {'corners': 4, 'equal_sides': True, 'angles': 90}
    neural_input = np.array([0.8, 0.1, 0.7, 0.9])  # Numerical features
    
    print("🧠 TOP-DOWN (Symbolic AI)")
    print("Input: Rules-based properties")
    symbolic_ai = SymbolicAI()
    sym_result, sym_conf = symbolic_ai.classify(symbolic_input)
    print(f"✓ Result: {sym_result} ({sym_conf}% confidence)")
    print("✓ Explainable: Can show exact reasoning steps")
    
    print("\n🔗 BOTTOM-UP (Neural Network)")
    print("Input: Numerical feature vector")
    neural_ai = NeuralNetwork()
    nn_result, nn_conf = neural_ai.classify(neural_input)
    print(f"⚫ Result: {nn_result} ({nn_conf:.1f}% confidence)")
    print("⚫ Black box: Cannot explain decision process")

# Run comparison
compare_approaches()

"""
Expected Output:
🧠 TOP-DOWN (Symbolic AI)
Input: Rules-based properties
✓ Result: square (100.0% confidence)
✓ Explainable: Can show exact reasoning steps

🔗 BOTTOM-UP (Neural Network)
Input: Numerical feature vector
⚫ Result: square (42.5% confidence)  
⚫ Black box: Cannot explain decision process
"""