from SPARQLWrapper import SPARQLWrapper, JSON

fuseki_url = "http://localhost:3030/ds/query"
sparql = SPARQLWrapper(fuseki_url)


def execute_sparql(query):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
