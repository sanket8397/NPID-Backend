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