import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Reading the weather dataset
print("Ensure 'weather_prediction_dataset.csv' is in the current directory.")
df = pd.read_csv('weather_prediction_dataset.csv')

# Simple preprocessing: drop NA, sort by date and location
df = df.dropna(subset=['TOURS_temp_mean', 'TOURS_humidity', 'TOURS_pressure', 'TOURS_wind_speed'])
df = df.sort_values(['DATE'])

print(df.head())
# Shift 'mean_temp' for next day prediction, group by location
df['next_day_temp'] = df['TOURS_temp_mean'].shift(-1)
df = df.dropna(subset=['next_day_temp'])

# Feature & target selection
features = ['TOURS_temp_mean', 'TOURS_humidity', 'TOURS_pressure', 'TOURS_wind_speed']
X = df[features]
y = df['next_day_temp']

# # Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Dumping and loading the model
joblib.dump(model, 'weather_regression_model.joblib')
loaded_model = joblib.load('weather_regression_model.joblib')

# # Example prediction
sample = X_test.iloc[0]
pred = loaded_model.predict([sample])[0]
print(f"Predicted next day's mean temperature: {pred:.1f}°C")
