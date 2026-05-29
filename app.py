from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib
import os

app = Flask(__name__)

# LOAD MODEL
model = tf.keras.models.load_model("weather_model.h5", compile=False)

# LOAD SCALER
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return "API is running 🚀"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    temperature = data['temperature']
    humidity = data['humidity']
    rain = data['rain']

    input_data = np.array([
        [temperature, humidity, rain],
        [temperature, humidity, rain],
        [temperature, humidity, rain],
        [temperature, humidity, rain],
        [temperature, humidity, rain]
    ])

    input_scaled = scaler.transform(input_data)
    input_scaled = np.expand_dims(input_scaled, axis=0)

    prediction = model.predict(input_scaled)
    result = scaler.inverse_transform(prediction)

    return jsonify({
        "temperature": float(result[0][0]),
        "humidity": float(result[0][1]),
        "rain": float(result[0][2])
    })

# مهم ل Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)