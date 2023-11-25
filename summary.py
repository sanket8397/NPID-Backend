from query_generator import *
from utils import *

def get_map_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
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

def get_gender_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_gender_query(years)
    results = execute_sparql(query)
    # print(results)

    victim_data = []
    for result in results["results"]["bindings"]:
        gender = result["gender"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["gender"] = "Male" if gender == "M" else "Female" 
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data

def get_race_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_race_query(years)
    results = execute_sparql(query)
    # print(results)

    race_mapping = {"W": "White", "H": "Hispanic", "A": "Asian", "B": "Black", "N": "Native American", "O": "Other"}

    victim_data = []
    for result in results["results"]["bindings"]:
        race = result["race"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["race"] = race_mapping[race] 
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data

def get_manner_of_death_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_manner_of_death_query(years)
    results = execute_sparql(query)
    # print(results)

    victim_data = []
    for result in results["results"]["bindings"]:
        manner_of_death = result["manner_of_death"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["manner_of_death"] = manner_of_death
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data

def get_armed_with_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_armed_with_query(years)
    results = execute_sparql(query)
    # print(results)

    victim_data = []
    for result in results["results"]["bindings"]:
        weapon = result["weapon"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["weapon"] = weapon
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data

def get_fleeing_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_fleeing_query(years)
    results = execute_sparql(query)
    # print(results)

    victim_data = []
    for result in results["results"]["bindings"]:
        fleeing = result["fleeing"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["fleeing"] = fleeing
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data

def get_mental_illness_data(years_list):
    if not years_list:
        years_list = ['2015', '2016', '2017']
    years = ' ,'.join(years_list)
    print(years)
    query = get_mental_illness_query(years)
    results = execute_sparql(query)
    # print(results)

    victim_data = []
    for result in results["results"]["bindings"]:
        mental_illness = result["mental_illness"]["value"]
        victim_cnt = result["victimCount"]["value"]
        victim_count = {}
        victim_count["mental_illness"] = "yes" if mental_illness == "true" else "no"
        victim_count["count"] = victim_cnt
        victim_data.append(victim_count)

    return victim_data