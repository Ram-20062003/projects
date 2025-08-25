# TOP-DOWN APPROACH (Symbolic AI) - Rule-Based
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

"""
Output:
✓ corners: 4
✓ equal_sides: True  
✓ angles: 90
Prediction: square (100.0% confidence)
"""