
import joblib
import numpy as np

try:
    model = joblib.load('models/model.pkl')
    print("Type:", type(model))
    
    if hasattr(model, 'steps'):
        print("Pipeline Steps:", [s[0] for s in model.steps])
        
        # Check for Scaler
        if 'scaler' in dict(model.steps):
            scaler = dict(model.steps)['scaler']
            print("Scaler Mean:", scaler.mean_)
            print("Scaler Scale:", scaler.scale_)
            
        # Check for Regressor
        if 'model' in dict(model.steps):
            reg = dict(model.steps)['model']
            print("Coef:", reg.coef_)
            print("Intercept:", reg.intercept_)
            
    # If it's just the regressor
    if hasattr(model, 'coef_'):
        print("Coef:", model.coef_)
        print("Intercept:", model.intercept_)

except Exception as e:
    print("Error:", e)
