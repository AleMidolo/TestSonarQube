def find_roots(graph, rdflib.RDFS.subClassOf):
    """
    restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    from rdflib import Graph, RDFS

    subclasses = set()
    parents = set()

    for s, p, o in graph:
        if p == rdflib.RDFS.subClassOf:
            subclasses.add(s)
            parents.add(o)

    roots = subclasses - parents
    return roots