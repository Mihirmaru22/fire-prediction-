import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

# Load Data
df = pd.read_csv('data/cleaned_forest_fires.csv')

# Features used in training (based on fwi-console.tsx and common sense)
# 'Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'Classes', 'Region'
features = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'Classes', 'Region']
target = 'FWI'

X = df[features]
y = df[target]

# Load Model
model = joblib.load('models/model.pkl')

# Predict
y_pred = model.predict(X)

# Calculate MSE
mse = mean_squared_error(y, y_pred)
print(f"MSE: {mse}")
