from flask import Flask, jsonify
from summary import *

app = Flask(__name__)

# Define a sample API endpoint


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route('/api/map', methods=['GET'])
def map_route():
    return jsonify(get_map_data())


if __name__ == '__main__':
    app.run(debug=True)
