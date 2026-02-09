import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

ages = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]).reshape(-1, 1)
blood_sugar = np.array([85, 88, 92, 95, 98, 105, 110, 115, 120, 125, 130, 135, 140, 145])

model = LinearRegression()
model.fit(ages, blood_sugar)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
