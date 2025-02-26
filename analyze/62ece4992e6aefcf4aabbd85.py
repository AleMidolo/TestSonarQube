def find_roots(graph, rdflib.RDFS.subClassOf):
    """
    restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    from rdflib import Graph, RDFS

    subclasses = set()
    parents = set()

    for child, _, parent in graph.triples((None, rdflib.RDFS.subClassOf, None)):
        subclasses.add(child)
        parents.add(parent)

    roots = subclasses - parents
    return roots