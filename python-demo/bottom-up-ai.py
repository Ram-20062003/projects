# BOTTOM-UP APPROACH (Connectionist AI) - Neural Network with 8 Input Features
import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Initialize random weights (normally learned from training data)
        np.random.seed(42)
        # Now 8 input features to 5 hidden neurons (you can adjust hidden size as needed)
        self.weights_input_hidden = np.random.randn(8, 5) * 0.5
        # 5 hidden neurons to 3 output classes
        self.weights_hidden_output = np.random.randn(5, 3) * 0.5
        self.bias_hidden = np.random.randn(5) * 0.1
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
# Features: [f1, f2, f3, f4, f5, f6, f7, f8]
test_features = np.array([0.8, 0.1, 0.7, 0.9, 0.5, 0.2, 0.4, 0.6])
result, confidence = nn.classify(test_features)
print(f"Prediction: {result} ({confidence:.1f}% confidence)")
