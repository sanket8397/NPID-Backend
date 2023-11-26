prefixes = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ont: <http://www.semanticweb.org/keyapatel/ontologies/2023/9/police-killings#>
"""

######################### Summary Queries ############################


def get_map_query(years):
    query = f"""
            {prefixes}

            SELECT ?stateName (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:livesInState ?state.
                ?state ont:hasStateName ?stateName.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?stateName
        """
    return query

def get_gender_query(years):
    query = f"""
            {prefixes}

            SELECT ?gender (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:hasGender ?gender.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?gender
        """
    return query

def get_race_query(years):
    query = f"""
            {prefixes}

            SELECT ?race (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:hasRace ?race.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?race
        """
    return query

def get_manner_of_death_query(years):
    query = f"""
            {prefixes}

            SELECT ?manner_of_death (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:mannerOfDeath ?manner_of_death.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?manner_of_death
        """
    return query

def get_armed_with_query(years):
    query = f"""
            {prefixes}

            SELECT ?weapon (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:wasArmedWith ?weapon.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?weapon
        """
    return query

def get_fleeing_query(years):
    query = f"""
            {prefixes}

            SELECT ?fleeing (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:wasFleeing ?fleeing.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?fleeing
        """
    return query

def get_mental_illness_query(years):
    query = f"""
            {prefixes}

            SELECT ?mental_illness (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?deathyear.
                ?victim ont:hasMentalIllness ?mental_illness.
                FILTER(?deathyear IN ({years}))
            }}
            GROUP BY ?mental_illness
        """
    return query

######################### Summary Queries ############################

######################### State City Queries ############################

def get_cities_query(state):
    query = f"""
            {prefixes}

            SELECT ?cityName
            WHERE {{
                ?state rdf:type ont:state.
                ?state ont:hasStateName "{state}".
                ?state ont:hasCity ?city.
                ?city ont:cityName ?cityName.
            }}
        """
    return query

def get_median_income_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName (str(?medianIncome) as ?median_income)
            WHERE {{
                ?city ont:cityName ?cityName.
                ?city ont:medianHousehold ?medianIncome.
                FILTER(?cityName IN ({cities}))
            }}
        """
    return query

def get_poverty_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName (str(?PovertyRate) as ?poverty_rate)
            WHERE {{
                ?city ont:cityName ?cityName.
                ?city ont:PovertyRate ?PovertyRate.
                FILTER(?cityName IN ({cities}))
            }}
        """
    return query

def get_highschool_grad_rate_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName (str(?highSchoolGrad) as ?highschool_grad_rate)
            WHERE {{
                ?city ont:cityName ?cityName.
                ?city ont:highSchoolGradRate ?highSchoolGrad.
                FILTER(?cityName IN ({cities}))
            }}
        """
    return query

def get_cities_count_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:livesInCity ?city.
                ?city ont:cityName ?cityName.
                FILTER(?cityName IN ({cities}))
            }}
            GROUP BY ?cityName
        """
    return query

def get_cities_race_distribution_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName 
                    (str(?asiandemo) as ?asian) 
                    (str(?blackdemo) as ?black)
                    (str(?hispanicdemo) as ?hispanic)
                    (str(?nativeamericandemo) as ?nativeamerican)
                    (str(?whitedemo) as ?white)
            WHERE {{
                ?city ont:cityName ?cityName.
                ?city ont:hasDemographicDetails ?demo.
                ?demo ont:hasAsian ?asiandemo.
                ?demo ont:hasBlack ?blackdemo.
                ?demo ont:hasHispanic ?hispanicdemo.
                ?demo ont:hasNativeAmerican ?nativeamericandemo.
                ?demo ont:hasWhites ?whitedemo.
                FILTER(?cityName IN ({cities}))
            }}
        """
    return query

def get_cities_race_count_query(cities):
    query = f"""
            {prefixes}

            SELECT ?cityName ?race (str(COUNT(?victim)) as ?victimCount)
            WHERE {{
                ?city rdf:type ont:city .
                ?city ont:cityName ?cityName .
                ?victim rdf:type ont:victim .
                ?victim ont:livesInCity ?city .
                ?victim ont:hasRace ?race .
                FILTER(?cityName IN ({cities}))
            }}
            GROUP BY ?cityName ?race
        """
    return query

######################### State City Queries ############################

######################### Temporal Queries ############################

def get_year_count_query():
    query = f"""
            {prefixes}

            SELECT (STR(?year) as ?deathYear) (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
                ?victim rdf:type ont:victim.
                ?victim ont:deathYear ?year.
            }}
            GROUP BY ?year
            ORDER BY ?year
        """
    return query

def get_year_race_count_query():
    query = f"""
            {prefixes}

            SELECT (STR(?year) as ?deathYear) ?race (STR(COUNT(?victim)) AS ?victimCount)
            WHERE {{
            ?victim rdf:type ont:victim .
            ?victim ont:deathYear ?year .
            ?victim ont:hasRace ?race .
            }}
            GROUP BY ?year ?race
            ORDER BY ?year ?race
        """
    return query

######################### Temporal Queries ############################