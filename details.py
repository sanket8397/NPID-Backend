from query_generator import *
from utils import *

def get_victim_details_data():
    query = get_victim_details_query()
    results = execute_sparql(query)

    race_mapping = {"W": "White", "H": "Hispanic", "A": "Asian", "B": "Black", "N": "Native American", "O": "Other"}

    victim_data = []
    for result in results["results"]["bindings"]:
        victim = {}
        victim["name"] = result["name"]["value"]
        victim["race"] = race_mapping[result["race"]["value"]]
        victim["age"] = result["age"]["value"]
        victim["deathyear"] = result["year"]["value"]
        victim["gender"] = "Male" if result["gender"]["value"] == "M" else "Female"
        victim["mentalillness"] = "yes" if result["mentalillness"]["value"] == "true" else "no"
        victim["mannerofdeath"] = result["mannerofdeath"]["value"]
        victim["weapon"] = result["weapon"]["value"]
        victim_data.append(victim)

    return victim_data
