from query_generator import *
from utils import *

def get_cities_original(state):
    query = get_cities_query(state)
    results = execute_sparql(query)
    cities = []
    for result in results["results"]["bindings"]:
        state_city = result["cityName"]["value"]
        cities.append(state_city)
    return cities
    
def get_cities(state):
    query = get_cities_query(state)
    results = execute_sparql(query)
    cities = []
    for result in results["results"]["bindings"]:
        state_city = result["cityName"]["value"]
        city = state_city.split(" - ")[1]
        cities.append(city)
    return cities


def get_median_income(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_median_income_query(cities)
    results = execute_sparql(query)

    income_data = []
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        median_income = result["median_income"]["value"]
        city_income = {}
        city_income["city"] = city.split(" - ")[1]
        city_income["income"] = median_income
        income_data.append(city_income)

    return income_data

def get_poverty_rate(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_poverty_query(cities)
    results = execute_sparql(query)

    poverty_data = []
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        poverty_rate = result["poverty_rate"]["value"]
        city_poverty_rate = {}
        city_poverty_rate["city"] = city.split(" - ")[1]
        city_poverty_rate["poverty_rate"] = poverty_rate
        poverty_data.append(city_poverty_rate)

    return poverty_data

def get_highschool_grad_rate(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_highschool_grad_rate_query(cities)
    results = execute_sparql(query)

    highschool_grad_rate_data = []
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        highschool_grad_rate = result["highschool_grad_rate"]["value"]
        city_highschool_grad_rate = {}
        city_highschool_grad_rate["city"] = city.split(" - ")[1]
        city_highschool_grad_rate["highschool_grad_rate"] = highschool_grad_rate
        highschool_grad_rate_data.append(city_highschool_grad_rate)

    return highschool_grad_rate_data
