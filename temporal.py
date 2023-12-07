from query_generator import *
from utils import *


def get_temporal_data():
    query = get_year_count_query()
    results = execute_sparql(query)

    victim_data = {}
    for result in results["results"]["bindings"]:
        deathYear = result["deathYear"]["value"]
        victim_count = result["victimCount"]["value"]
        victim_data[deathYear] = int(victim_count)

    return victim_data


def get_year_race_count_data():
    query = get_year_race_count_query()
    results = execute_sparql(query)

    race_mapping = {"W": "White", "H": "Hispanic", "A": "Asian",
                    "B": "Black", "N": "Native American", "O": "Other"}

    victim_data = {}
    for result in results["results"]["bindings"]:
        deathYear = result["deathYear"]["value"]
        race = race_mapping[result["race"]["value"]]
        victim_count = result["victimCount"]["value"]
        if race not in victim_data:
            victim_data[race] = {}
        victim_data[race][deathYear] = int(victim_count)

    return victim_data
