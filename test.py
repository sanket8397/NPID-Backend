# from query_generator import *
# from utils import *

# query = get_map_query()
# results = execute_sparql(query)
# print(results)

# for result in results["results"]["bindings"]:
#     state_name = result["stateName"]["value"]
#     victim_count = result["victimCount"]["value"]
#     print(f"State: {state_name}, Victim Count: {victim_count}")

from state_city import *
a = get_cities_original('CA')
b = get_median_income(a)
print(b)