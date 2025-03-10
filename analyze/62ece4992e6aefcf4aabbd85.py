from rdflib import Graph, RDFS

def find_roots(graph, prop):
    """
    Restituisce un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    all_nodes = set(graph.subjects(prop, None))
    all_parents = set(graph.objects(None, prop))
    
    roots = all_nodes - all_parents
    return roots