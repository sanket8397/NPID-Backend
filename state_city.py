from query_generator import *
from utils import *


def get_states():
    query = get_states_query()
    results = execute_sparql(query)
    states = []
    for result in results["results"]["bindings"]:
        state = result["stateName"]["value"]
        states.append(state)
    return states


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
    death_count = get_cities_count_data(citiesList)
    income_data = []
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        median_income = result["median_income"]["value"]
        city_income = {}
        city = city.split(" - ")[1]
        city_income["city"] = city
        city_income["median_income"] = int(median_income)
        city_income["deaths"] = death_count[city]
        income_data.append(city_income)

    return income_data


def get_rates(citiesList):
    poverty_rate = get_poverty_rate(citiesList)
    grad_rate = get_highschool_grad_rate(citiesList)
    death_count = get_cities_count_data(citiesList)
    data = []
    for city in death_count:
        city_data = {}
        city_data["city"] = city
        city_data["poverty_rate"] = poverty_rate[city]
        city_data["percent_completed_hs"] = grad_rate[city]
        city_data["deaths"] = death_count[city]
        data.append(city_data)
    return data


def get_poverty_rate(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_poverty_query(cities)
    results = execute_sparql(query)

    poverty_data = {}
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        poverty_rate = result["poverty_rate"]["value"]
        poverty_data[city.split(" - ")[1]] = float(poverty_rate)

    return poverty_data


def get_highschool_grad_rate(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_highschool_grad_rate_query(cities)
    results = execute_sparql(query)

    highschool_grad_rate_data = {}
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        highschool_grad_rate = result["highschool_grad_rate"]["value"]
        city = city.split(" - ")[1]
        highschool_grad_rate_data[city] = float(highschool_grad_rate)

    return highschool_grad_rate_data


def get_cities_count_data(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_cities_count_query(cities)
    results = execute_sparql(query)

    city_victim_data = {}
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        victim_count = result["victimCount"]["value"]
        city_victim_data[city.split(" - ")[1]] = int(victim_count)

    return city_victim_data


def get_cities_race_data(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_cities_race_distribution_query(cities)
    results = execute_sparql(query)

    city_race_data = []
    for result in results["results"]["bindings"]:
        city_race = {}
        city_race["city"] = result["cityName"]["value"].split(" - ")[1]
        city_race["asian"] = float(result["asian"]["value"])
        city_race["black"] = float(result["black"]["value"])
        city_race["hispanic"] = float(result["hispanic"]["value"])
        city_race["nativeamerican"] = float(result["nativeamerican"]["value"])
        city_race["white"] = float(result["white"]["value"])
        city_race_data.append(city_race)

    return city_race_data


def get_cities_race_count_data(citiesList):
    cities = "', '".join(citiesList)
    cities = "'" + cities + "'"
    query = get_cities_race_count_query(cities)
    results = execute_sparql(query)

    race_mapping = {"W": "white", "H": "hispanic", "A": "asian",
                    "B": "black", "N": "nativeamerican", "O": "other"}

    city_victim_data = {}
    for result in results["results"]["bindings"]:
        city = result["cityName"]["value"]
        race = result["race"]["value"]
        victim_count = result["victimCount"]["value"]
        city = city.split(" - ")[1]
        if city not in city_victim_data:
            city_victim_data[city] = {}
        city_victim_data[city][race_mapping[race]] = int(victim_count)

    data = []
    for city in city_victim_data:
        temp = {'city': city, 'white': 0, 'black': 0,
                'nativeamerican': 0, 'asian': 0, 'hispanic': 0}
        for race in city_victim_data[city]:
            temp[race] = city_victim_data[city][race]
        data.append(temp)

    return data
