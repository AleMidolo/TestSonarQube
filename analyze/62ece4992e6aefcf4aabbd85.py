def find_roots(graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None) -> Set["Node"]:
    """
    Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader
    """
    # If roots not provided, get all subjects that appear as objects in triples with prop
    if roots is None:
        roots = set()
        for s, p, o in graph:
            if p == prop:
                roots.add(o)
                
    # Get all objects that appear as subjects in triples with prop
    children = set()
    for s, p, o in graph:
        if p == prop:
            children.add(s)
            
    # Roots are those that have no parents
    return roots - children