from flask import Flask, jsonify, request
from summary import *

app = Flask(__name__)

# Define a sample API endpoint


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# http://127.0.0.1:5000/api/map?year=2015&year=2016&year=2017
# http://127.0.0.1:5000/api/map
@app.route('/api/map', methods=['GET'])
def map_route():
    years_list = request.args.getlist('year')
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    return jsonify(get_map_data(years))


if __name__ == '__main__':
    app.run(debug=True)
