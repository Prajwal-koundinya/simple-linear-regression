Blood Sugar Predictor

Setup Instructions:

1. Install requirements:
   pip install scikit-learn flask

2. Train the model:
   python train_model.py

3. Run the Flask app:
   python app.py

4. Open your browser and go to:
   http://127.0.0.1:5000

Usage:
- Enter age in the input field
- Click "Predict" button
- View predicted blood sugar level and diagnosis

Diagnosis Categories:
- Normal: Blood sugar < 100 mg/dL
- Prediabetes: Blood sugar 100-125 mg/dL
- Diabetes: Blood sugar >= 126 mg/dL
