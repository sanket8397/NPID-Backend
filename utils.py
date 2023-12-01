from SPARQLWrapper import SPARQLWrapper, JSON

fuseki_url = "http://23.22.158.11:3030/ds/query"
sparql = SPARQLWrapper(fuseki_url)


def execute_sparql(query):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
