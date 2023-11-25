prefixes = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ont: <http://www.semanticweb.org/keyapatel/ontologies/2023/9/police-killings#>
"""


def get_map_query(years):
    map_query = f"""
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
    return map_query
