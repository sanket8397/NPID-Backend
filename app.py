from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from summary import *
from state_city import *
from temporal import *
from details import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/api/hello', methods=['GET'])
@cross_origin(supports_credentials=True)
def hello():
    return jsonify({"message": "Hello, World!"})

######################### Summary routes ############################

# http://127.0.0.1:5000/api/summary/map?year=2015&year=2016&year=2017
# http://127.0.0.1:5000/api/summary/map


@app.route('/api/summary/map', methods=['GET'])
@cross_origin(supports_credentials=True)
def map_route():
    years_list = request.args.getlist('year')
    return jsonify(get_map_data(years_list))


@app.route('/api/summary/gender', methods=['GET'])
@cross_origin(supports_credentials=True)
def gender_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    return jsonify(get_gender_data(years_list, state))


@app.route('/api/summary/race', methods=['GET'])
@cross_origin(supports_credentials=True)
def race_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    print(state)
    return jsonify(get_race_data(years_list, state))


@app.route('/api/summary/mannerofdeath', methods=['GET'])
@cross_origin(supports_credentials=True)
def manner_of_death_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    return jsonify(get_manner_of_death_data(years_list, state))


@app.route('/api/summary/armedwith', methods=['GET'])
@cross_origin(supports_credentials=True)
def armed_with_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    return jsonify(get_armed_with_data(years_list, state))


@app.route('/api/summary/fleeing', methods=['GET'])
@cross_origin(supports_credentials=True)
def fleeing_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    return jsonify(get_fleeing_data(years_list, state))


@app.route('/api/summary/mentalillness', methods=['GET'])
@cross_origin(supports_credentials=True)
def mental_illness_route():
    years_list = request.args.getlist('year')
    state = request.args.get('state')
    return jsonify(get_mental_illness_data(years_list, state))

######################### Summary routes ############################

######################### State City routes ############################


@app.route('/api/statecity/states', methods=['GET'])
@cross_origin(supports_credentials=True)
def states_route():
    return jsonify(get_states())


@app.route('/api/statecity/cities', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_route():
    state = request.args.get('state')
    return jsonify(get_cities(state))


@app.route('/api/statecity/income', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_income_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_median_income(cities))


@app.route('/api/statecity/poverty', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_poverty_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_poverty_rate(cities))


@app.route('/api/statecity/gradrate', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_highschool_grad_rate_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_highschool_grad_rate(cities))


@app.route('/api/statecity/rates', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_rate_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_rates(cities))


@app.route('/api/statecity/cityvictimcount', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_count_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_cities_count_data(cities))


@app.route('/api/statecity/cityrace', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_race_distribution_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_cities_race_data(cities))


@app.route('/api/statecity/cityracevictimcount', methods=['GET'])
@cross_origin(supports_credentials=True)
def cities_race_count_route():
    state = request.args.get('state')
    cities = get_cities_original(state)
    return jsonify(get_cities_race_count_data(cities))

######################### State City routes ############################

######################### Temporal Routes ############################


@app.route('/api/temporal/count', methods=['GET'])
@cross_origin(supports_credentials=True)
def temporal_count_route():
    return jsonify(get_temporal_data())


@app.route('/api/temporal/racecount', methods=['GET'])
@cross_origin(supports_credentials=True)
def temporal_race_count_route():
    return jsonify(get_year_race_count_data())

######################### Temporal Routes ############################

######################### Details Routes ############################


@app.route('/api/details', methods=['GET'])
@cross_origin(supports_credentials=True)
def details_route():
    return jsonify(get_victim_details_data())

######################### Details Routes ############################


if __name__ == '__main__':
    app.run(debug=True)
