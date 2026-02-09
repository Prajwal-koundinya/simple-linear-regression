from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    prediction = model.predict(np.array([[age]]))[0]
    
    if prediction >= 126:
        diagnosis = "Diabetes"
    elif prediction >= 100:
        diagnosis = "Prediabetes"
    else:
        diagnosis = "Normal"
    
    return jsonify({
        'blood_sugar': round(prediction, 2),
        'diagnosis': diagnosis
    })

if __name__ == '__main__':
    app.run(debug=True)
