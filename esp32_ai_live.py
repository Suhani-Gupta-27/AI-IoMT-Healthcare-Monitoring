import serial
import joblib
import numpy as np
import pandas as pd

# CHANGE COM PORT if needed (COM6 / COM7 etc)
ser = serial.Serial("COM6", 9600, timeout=1)

model = joblib.load("iomt_ai_model.pkl")

print("🔌 Connected to ESP32")

while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        if not line:
            continue

        print("\nRaw ESP32 data:", line)

        temp, pulse, ldr = map(float, line.split(","))

        input_data = pd.DataFrame(
            [[temp, pulse, ldr]],
            columns=["Temperature", "Pulse", "LDR"]
        )

        prediction = model.predict(input_data)

        light, drug = prediction[0]

        print("\n--- LIVE SENSOR READINGS ---")
        print(f"Temperature : {temp} °C")
        print(f"Pulse       : {pulse} bpm")
        print(f"LDR Value   : {ldr}")

        print("\n--- AI RECOMMENDATION ---")
        print(f"Increase Light by : {light:.2f} %")
        print(f"Increase Drug by  : {drug:.2f} units")


    except Exception as e:
        print("Error:", e)