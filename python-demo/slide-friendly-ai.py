# SLIDE-FRIENDLY: AI APPROACHES COMPARISON

# ===== TOP-DOWN APPROACH =====
class SymbolicAI:
    rules = {
        'square': {'corners': 4, 'equal_sides': True},
        'circle': {'corners': 0, 'curves': True}
    }
    
    def classify(self, properties):
        # Check rules step by step
        for shape, rules in self.rules.items():
            if all(properties.get(k) == v for k, v in rules.items()):
                return shape, "100% - Can explain why!"

# Example
ai = SymbolicAI()
result = ai.classify({'corners': 4, 'equal_sides': True})
print(f"Top-Down: {result}")

# ===== BOTTOM-UP APPROACH =====
import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Simulated learned weights
        self.weights = np.random.randn(3, 2) * 0.5
    
    def classify(self, features):
        # Mathematical transformation (simplified)
        output = 1 / (1 + np.exp(-np.dot(features, self.weights)))
        confidence = max(output) * 100
        return "square", f"{confidence:.1f}% - Cannot explain why!"

# Example  
nn = NeuralNetwork()
result = nn.classify(np.array([0.8, 0.9, 0.7]))
print(f"Bottom-Up: {result}")

# ===== KEY INSIGHT =====
# Top-Down: IF corners==4 AND equal_sides==True THEN square ✓
# Bottom-Up: sigmoid(features * weights) = prediction ⚫