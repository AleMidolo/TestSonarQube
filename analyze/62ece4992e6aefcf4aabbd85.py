def find_roots(graph, rdflib.RDFS.subClassOf):
    """
    restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    from rdflib import Graph, RDFS

    # Trova tutti i soggetti che hanno una relazione di sottoclasse
    subclasses = set(graph.subjects(predicate=rdflib.RDFS.subClassOf))

    # Trova tutti i soggetti che non sono figli di nessun altro
    all_classes = set(graph.subjects())
    roots = all_classes - subclasses

    return roots