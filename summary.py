from query_generator import *
from utils import *

# Year functionality yet to add
def get_map_data(years):
    query = get_map_query(years)
    results = execute_sparql(query)
    # print(results)

    state_victim_data = []
    for result in results["results"]["bindings"]:
        state_name = result["stateName"]["value"]
        victim_count = result["victimCount"]["value"]
        state_victim_count = {}
        state_victim_count["name"] = state_name
        state_victim_count["count"] = victim_count
        state_victim_data.append(state_victim_count)

    return state_victim_data
