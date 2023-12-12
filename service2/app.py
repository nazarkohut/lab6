# service2.py

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify(message='Service2 is alive!')


@app.route('/data')
def get_data():
    # Logic to get data in Service2
    data = {'example_key': 'example_value'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
