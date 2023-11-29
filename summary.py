from query_generator import *
from utils import *


def get_map_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    query = get_map_query(years)
    results = execute_sparql(query)

    state_victim_data = []
    for result in results["results"]["bindings"]:
        state_name = result["stateName"]["value"]
        victim_count = result["victimCount"]["value"]
        state_victim_count = {}
        state_victim_count["name"] = state_name
        state_victim_count["count"] = victim_count
        state_victim_data.append(state_victim_count)

    return state_victim_data


def get_gender_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_gender_query(years)
    if state:
        query = get_gender_state_query(years, state)
    results = execute_sparql(query)

    victim_data = {}
    for result in results["results"]["bindings"]:
        gender = "Male" if result["gender"]["value"] == "M" else "Female"
        victim_cnt = result["victimCount"]["value"]
        victim_data[gender] = int(victim_cnt)

    return victim_data


def get_race_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_race_query(years)
    if state:
        query = get_race_state_query(years, state)
    results = execute_sparql(query)

    race_mapping = {"W": "White", "H": "Hispanic", "A": "Asian",
                    "B": "Black", "N": "Native American", "O": "Other"}

    victim_data = {}
    for result in results["results"]["bindings"]:
        race = result["race"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_data[race_mapping[race]] = int(victim_cnt)

    return victim_data


def get_manner_of_death_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_manner_of_death_query(years)
    if state:
        query = get_manner_of_death_state_query(years, state)
    results = execute_sparql(query)

    victim_data = {}
    for result in results["results"]["bindings"]:
        manner_of_death = result["manner_of_death"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_data[manner_of_death] = int(victim_cnt)

    return victim_data


def get_armed_with_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_armed_with_query(years)
    if state:
        query = get_armed_with_state_query(years, state)
    results = execute_sparql(query)

    victim_data = []
    for result in results["results"]["bindings"]:
        weapon = result["weapon"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["weapon"] = weapon
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data


def get_fleeing_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_fleeing_query(years)
    if state:
        query = get_fleeing_state_query(years, state)
    results = execute_sparql(query)

    victim_data = {}
    for result in results["results"]["bindings"]:
        fleeing = result["fleeing"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_data[fleeing] = int(victim_cnt)

    return victim_data


def get_mental_illness_data(years_list, state):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)

    query = get_mental_illness_query(years)
    if state:
        query = get_mental_illness_state_query(years, state)
    results = execute_sparql(query)

    victim_data = {}
    for result in results["results"]["bindings"]:
        mental_illness = "yes" if result["mental_illness"]["value"] == "true" else "no"
        victim_cnt = result["victimCount"]["value"]
        victim_data[mental_illness] = int(victim_cnt)

    return victim_data
