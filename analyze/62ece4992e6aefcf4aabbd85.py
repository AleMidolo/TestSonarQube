def find_roots(graph, rdflib.RDFS.subClassOf):
    roots = set()
    subclasses = set()

    for s, p, o in graph:
        if p == rdflib.RDFS.subClassOf:
            subclasses.add(s)

    for s in subclasses:
        if (s, rdflib.RDFS.subClassOf, None) not in graph:
            roots.add(s)

    return roots