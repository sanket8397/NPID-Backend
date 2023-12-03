from SPARQLWrapper import SPARQLWrapper, JSON
import os

fuseki_url = os.getenv('FUSEKI_URL', 'http://127.0.0.1:3030/ds/query')
sparql = SPARQLWrapper(fuseki_url)


def execute_sparql(query):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
