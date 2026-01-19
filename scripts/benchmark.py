import joblib
import pandas as pd
import time

model = joblib.load('models/model.pkl')
feature_names = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'Classes', 'Region']

sample = [30, 50, 15, 0.0, 80.0, 10.0, 20.0, 5.0, 10.0, 1, 1]
sample_df = pd.DataFrame([sample], columns=feature_names)
start_time = time.time()

for _ in range(1000):
    model.predict(sample_df)

end_time = time.time()

avg_ms = (end_time - start_time) / 1000 * 1000
print(f"Average prediction time over 1000 runs: {avg_ms:.4f} ms")