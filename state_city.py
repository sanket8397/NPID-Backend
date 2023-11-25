from query_generator import *
from utils import *

def get_cities(state):
    query = get_cities_query(state)
    results = execute_sparql(query)
    cities = []
    for result in results["results"]["bindings"]:
        state_city = result["cityName"]["value"]
        city = state_city.split(" - ")[1]
        cities.append(city)
    return cities