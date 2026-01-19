import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


df = pd.read_csv("data_set/cleaned_forest_fires.csv")

'''

Expected Features: ['Temperature' 'RH' 'Ws' 'Rain' 'FFMC' 'DMC' 'DC' 'ISI' 'BUI' 'Classes'
 'Region']

'''
X = df.drop(columns=['FWI','day','month','year'])
y = df['FWI']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = joblib.load('models/model.pkl')

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"Mean Squared Error: {mse:.4f}")