from rdflib import Graph, RDFS

def find_roots(graph, prop):
    """
    Restituisce un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    roots = set()
    all_subjects = set(graph.subjects(predicate=prop))
    all_objects = set(graph.objects(predicate=prop))
    
    # Le radici sono quei soggetti che non compaiono come oggetti in nessuna tripla
    roots = all_subjects - all_objects
    
    return roots