from flask import Flask, jsonify, request
from summary import *

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# http://127.0.0.1:5000/api/summary/map?year=2015&year=2016&year=2017
# http://127.0.0.1:5000/api/summary/map

@app.route('/api/summary/map', methods=['GET'])
def map_route():
    years_list = request.args.getlist('year')
    return jsonify(get_map_data(years_list))

@app.route('/api/summary/gender', methods=['GET'])
def gender_route():
    years_list = request.args.getlist('year')
    return jsonify(get_gender_data(years_list))

@app.route('/api/summary/race', methods=['GET'])
def race_route():
    years_list = request.args.getlist('year')
    return jsonify(get_race_data(years_list))

@app.route('/api/summary/mannerofdeath', methods=['GET'])
def manner_of_death_route():
    years_list = request.args.getlist('year')
    return jsonify(get_manner_of_death_data(years_list))

@app.route('/api/summary/armedwith', methods=['GET'])
def armed_with_route():
    years_list = request.args.getlist('year')
    return jsonify(get_armed_with_data(years_list))

@app.route('/api/summary/fleeing', methods=['GET'])
def fleeing_route():
    years_list = request.args.getlist('year')
    return jsonify(get_fleeing_data(years_list))

if __name__ == '__main__':
    app.run(debug=True)
