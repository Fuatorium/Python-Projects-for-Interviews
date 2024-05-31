from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import pickle

app = Flask(__name__)

model = pickle.load(open('models/kmeans_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))
gender_encoder = pickle.load(open('models/gender_encoder.pkl', 'rb'))
profession_encoder = pickle.load(open('models/profession_encoder.pkl', 'rb'))
segment_descriptions = pickle.load(open('models/segment_descriptions.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    try:
        data['Gender'] = gender_encoder.transform([data['Gender']])[0]
    except ValueError:
        return jsonify(error="Geçersiz cinsiyet değeri")
    try:
        data['Profession'] = profession_encoder.transform([data['Profession']])[0]
    except ValueError:
        return jsonify(error="Geçersiz meslek değeri")
    input_data = np.array([
        data['Age'], 
        data['Gender'], 
        data['Annual Income ($)'], 
        data['Spending Score (1-100)'], 
        data['Profession'],
        data['Work Experience'], 
        data['Family Size']
    ], dtype=float)
    input_data = scaler.transform([input_data])
    segment = model.predict(input_data)[0]
    segment_description = segment_descriptions[segment]
    return jsonify(segment=int(segment), description=segment_description)

@app.route('/segments')
def segments():
    return render_template('segments.html', segment_descriptions=segment_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
