import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("training_data.csv")

X = data[["Temperature", "Pulse", "LDR"]]
y = data[["Light", "Drug"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "iomt_ai_model.pkl")

print("AI model trained successfully")