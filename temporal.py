from query_generator import *
from utils import *

def get_temporal_data():
    query = get_year_count_query()
    results = execute_sparql(query)

    victim_data = []
    for result in results["results"]["bindings"]:
        deathYear = result["deathYear"]["value"]
        victim_count = result["victimCount"]["value"]
        year_victim_count = {}
        year_victim_count["year"] = deathYear
        year_victim_count["count"] = victim_count
        victim_data.append(year_victim_count)

    return victim_data

def get_year_race_count_data():
    query = get_year_race_count_query()
    results = execute_sparql(query)

    race_mapping = {"W": "White", "H": "Hispanic", "A": "Asian", "B": "Black", "N": "Native American", "O": "Other"}

    year_victim_data = []
    for result in results["results"]["bindings"]:
        deathYear = result["deathYear"]["value"]
        race = result["race"]["value"]
        victim_count = result["victimCount"]["value"]
        year_victim_count = {}
        year_victim_count["year"] = deathYear
        year_victim_count["race"] = race_mapping[race]
        year_victim_count["count"] = victim_count
        year_victim_data.append(year_victim_count)

    return year_victim_data