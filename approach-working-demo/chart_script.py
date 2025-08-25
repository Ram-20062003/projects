import plotly.graph_objects as go
import pandas as pd

# Load the data
data = [
    {"aspect": "Data Representation", "top_down": "Symbolic rules (corners: 4, curves: 0)", "bottom_up": "Numerical features [0.9, 0.1, 0.9, 0.9...]"},
    {"aspect": "Decision Process", "top_down": "IF-THEN logical evaluation", "bottom_up": "Mathematical transformations"},
    {"aspect": "Confidence Calculation", "top_down": "% of rules matched (75% = 3/4 rules)", "bottom_up": "Network activation strength (0.89)"},
    {"aspect": "Explainability", "top_down": "Can explain reasoning step-by-step", "bottom_up": "Black box - cannot explain why"},
    {"aspect": "Learning Method", "top_down": "Expert-programmed rules", "bottom_up": "Learned from training data"},
    {"aspect": "Processing Style", "top_down": "Discrete rule matching", "bottom_up": "Continuous numerical processing"}
]

# Convert to DataFrame for easier handling
df = pd.DataFrame(data)

# Use more descriptive text while keeping it readable
aspect_names = [
    "Data Repr",
    "Decision", 
    "Confidence",
    "Explain",
    "Learning",
    "Processing"
]

top_down_text = [
    "Symbolic rules<br>(corners: 4, curves: 0)",
    "IF-THEN logical<br>evaluation", 
    "% rules matched<br>(75% = 3/4 rules)",
    "Can explain reasoning<br>step-by-step",
    "Expert-programmed<br>rules",
    "Discrete rule<br>matching"
]

bottom_up_text = [
    "Numerical features<br>[0.9, 0.1, 0.9, 0.9...]",
    "Mathematical<br>transformations",
    "Network activation<br>strength (0.89)",
    "Black box - cannot<br>explain why",
    "Learned from<br>training data", 
    "Continuous numerical<br>processing"
]

# Create the table
fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Aspect</b>', '<b>Top-Down</b>', '<b>Bottom-Up</b>'],
        fill_color=['#f0f0f0', '#1FB8CD', '#DB4545'],
        align='center',
        font=dict(color=['black', 'white', 'white'], size=16),
        height=50
    ),
    cells=dict(
        values=[
            aspect_names,
            top_down_text,
            bottom_up_text
        ],
        fill_color=[['#f8f8f8']*6, ['rgba(31, 184, 205, 0.1)']*6, ['rgba(219, 69, 69, 0.1)']*6],
        align=['center', 'left', 'left'],
        font=dict(color=['black', 'black', 'black'], size=13),
        height=60,
        line=dict(color='#e0e0e0', width=1)
    )
)])

fig.update_layout(
    title="Top-Down vs Bottom-Up Approaches"
)

fig.write_image("comparison_table.png")