prefixes = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ont: <http://www.semanticweb.org/keyapatel/ontologies/2023/9/police-killings#>
"""


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