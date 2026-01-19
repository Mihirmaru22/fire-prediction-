from flask import Flask, request, render_template
import joblib
import numpy as np

application = Flask(__name__)
app = application

# 1. Load the Model Pipeline (includes Scaler + Model)
model = joblib.load('models/model.pkl')

# 2. Define exactly 11 features (Must match your training data columns)
FEATURES = [
    'Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 
    'DMC', 'DC', 'ISI', 'BUI', 'Classes', 'Region'
]

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:
            # 3. Collect all 11 inputs from the form
            data = [float(request.form[field]) for field in FEATURES]
            
            # 4. Predict (The pipeline handles scaling automatically)
            prediction = model.predict([data])[0]

            return render_template("home1.html", result=round(prediction, 2))
            
        except Exception as e:
            return render_template("home1.html", result=f"Error: {e}")
    else:
        return render_template("home1.html")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)

