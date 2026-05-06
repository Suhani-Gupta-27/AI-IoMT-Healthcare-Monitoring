import random
import csv

with open("training_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Temperature", "Pulse", "LDR", "Light", "Drug"])

    for _ in range(1000):
        temp = round(random.uniform(36.0, 40.5), 2)
        pulse = random.randint(60, 130)
        ldr = random.randint(150, 450)

        if temp < 37:
            drug = 0
        elif temp < 38:
            drug = random.randint(1, 3)
        elif temp < 39:
            drug = random.randint(4, 7)
        else:
            drug = random.randint(8, 15)

        if pulse > 100:
            drug += 2

        if ldr < 250:
            light = random.randint(40, 80)
        elif ldr < 350:
            light = random.randint(15, 40)
        else:
            light = random.randint(0, 10)

        writer.writerow([temp, pulse, ldr, light, drug])

print("Training data generated")