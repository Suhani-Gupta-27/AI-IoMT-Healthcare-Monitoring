import joblib
import numpy as np

model = joblib.load("iomt_ai_model.pkl")

# Example sensor readings
temp = 38.5
pulse = 104
ldr = 230

input_data = np.array([[temp, pulse, ldr]])
prediction = model.predict(input_data)

print("\n--- SENSOR READINGS ---")
print(f"Temperature : {temp} °C")
print(f"Pulse       : {pulse} bpm")
print(f"LDR Value   : {ldr}")

print("\n--- AI RECOMMENDATION ---")
print(f"Increase Photothermal Light by : {prediction[0][0]:.2f} %")
print(f"Increase Drug Dosage by        : {prediction[0][1]:.2f} units")
import csv
from datetime import datetime

with open("training_data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        datetime.now(),
        temp,
        pulse,
        ldr,
        prediction[0][0],
        prediction[0][1]
    ])