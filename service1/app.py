# service1.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify(message='Service1 is alive!')


@app.route('/get_data_from_service2')
def get_data_from_service2():
    # Assuming Service2 is running on http://service2:5001
    service2_url = 'http://service2:5001/data'

    try:
        response = requests.get(service2_url)
        data_from_service2 = response.json()
        return jsonify(data_from_service2)
    except requests.exceptions.RequestException as e:
        return jsonify(error=f"Error connecting to Service2: {str(e)}"), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
