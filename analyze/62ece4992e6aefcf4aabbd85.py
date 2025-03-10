from rdflib import Graph, RDFS

def find_roots(graph, prop):
    """
    Restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    roots = set()
    all_subjects = set(graph.subjects(prop, None))
    all_objects = set(graph.objects(None, prop))
    
    # Roots are subjects that are not objects in any triple
    roots = all_subjects - all_objects
    
    return roots