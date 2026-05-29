from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    temperature = data['temperature']
    humidity = data['humidity']
    rain = data['rain']

    # نتيجة بسيطة (mock)
    return jsonify({
        "temperature": temperature + 1,
        "humidity": humidity,
        "rain": rain
    })

if __name__ == "__main__":
    app.run()
