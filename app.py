from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file
csv_file = 'Data/PoliceKillingsUS.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file, encoding='latin-1')

# Extract unique states and cities
states = df['state'].unique()
cities = df['city'].unique()

# Define an endpoint to get a list of unique states
@app.route('/states', methods=['GET'])
def get_states():
    return jsonify(states.tolist())

# Define an endpoint to get a list of unique cities
@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(cities.tolist())

# Define an endpoint to get cities for a specific state
@app.route('/<state>', methods=['GET'])
def get_cities_by_state(state):
    cities_in_state = df[df['state'] == state]['city'].unique()
    return jsonify(cities_in_state.tolist())

if __name__ == '__main__':
    app.run(debug=True)