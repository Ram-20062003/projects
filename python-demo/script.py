# Create concise Python code examples for both AI approaches

top_down_code = '''# TOP-DOWN APPROACH (Symbolic AI) - Rule-Based
class SymbolicAI:
    def __init__(self):
        # Define explicit rules for each shape
        self.rules = {
            'square': {'corners': 4, 'equal_sides': True, 'angles': 90},
            'circle': {'corners': 0, 'curves': True, 'symmetry': 'radial'},
            'triangle': {'corners': 3, 'angles_sum': 180}
        }
    
    def classify(self, shape_properties):
        """Rule-based classification with explainable reasoning"""
        for shape_name, rules in self.rules.items():
            matches = 0
            total_rules = len(rules)
            
            # Check each rule
            for rule, expected_value in rules.items():
                if shape_properties.get(rule) == expected_value:
                    matches += 1
                    print(f"✓ {rule}: {expected_value}")
                else:
                    print(f"✗ {rule}: expected {expected_value}")
            
            # Calculate confidence
            confidence = (matches / total_rules) * 100
            if confidence >= 75:  # Threshold for classification
                return shape_name, confidence
        
        return "unknown", 0

# Example usage
ai = SymbolicAI()
test_shape = {'corners': 4, 'equal_sides': True, 'angles': 90}
result, confidence = ai.classify(test_shape)
print(f"Prediction: {result} ({confidence}% confidence)")
'''

bottom_up_code = '''# BOTTOM-UP APPROACH (Connectionist AI) - Neural Network
import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Initialize random weights (normally learned from training data)
        np.random.seed(42)
        self.weights_input_hidden = np.random.randn(4, 3) * 0.5
        self.weights_hidden_output = np.random.randn(3, 3) * 0.5
        self.bias_hidden = np.random.randn(3) * 0.1
        self.bias_output = np.random.randn(3) * 0.1
    
    def sigmoid(self, x):
        """Activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def forward(self, features):
        """Forward propagation through network"""
        # Input to hidden layer
        hidden_input = np.dot(features, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        
        # Hidden to output layer
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_input)
        
        return output, hidden_output
    
    def classify(self, features):
        """Neural network classification (black box)"""
        output, hidden = self.forward(features)
        classes = ['square', 'circle', 'triangle']
        
        # Highest activation wins
        prediction_idx = np.argmax(output)
        confidence = output[prediction_idx] * 100
        
        print(f"Hidden layer activations: {hidden.round(3)}")
        print(f"Output layer activations: {output.round(3)}")
        
        return classes[prediction_idx], confidence

# Example usage
nn = NeuralNetwork()
# Features: [corners, curves, symmetry, area_ratio]
test_features = np.array([0.8, 0.1, 0.7, 0.9])  # Square-like features
result, confidence = nn.classify(test_features)
print(f"Prediction: {result} ({confidence:.1f}% confidence)")
'''

comparison_code = '''# SIDE-BY-SIDE COMPARISON
def compare_approaches():
    """Demonstrate both approaches on same input"""
    
    # Same logical shape: Square
    symbolic_input = {'corners': 4, 'equal_sides': True, 'angles': 90}
    neural_input = np.array([0.8, 0.1, 0.7, 0.9])  # Numerical features
    
    print("=== TOP-DOWN (Symbolic AI) ===")
    symbolic_ai = SymbolicAI()
    sym_result, sym_conf = symbolic_ai.classify(symbolic_input)
    print(f"Result: {sym_result} ({sym_conf}% confidence)")
    print("Reasoning: Can explain every step!")
    
    print("\\n=== BOTTOM-UP (Neural Network) ===")
    neural_ai = NeuralNetwork()
    nn_result, nn_conf = neural_ai.classify(neural_input)
    print(f"Result: {nn_result} ({nn_conf:.1f}% confidence)")
    print("Reasoning: Black box - cannot explain why!")

compare_approaches()
'''

print("=== TOP-DOWN APPROACH CODE ===")
print(top_down_code)
print("\n" + "="*50)
print("=== BOTTOM-UP APPROACH CODE ===")
print(bottom_up_code)
print("\n" + "="*50)
print("=== COMPARISON DEMO CODE ===")
print(comparison_code)