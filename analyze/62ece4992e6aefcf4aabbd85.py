def find_roots(graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None) -> Set["Node"]:
    # If roots not provided, get all subjects that appear as objects in prop relationships
    if roots is None:
        roots = set()
        for s, p, o in graph.triples((None, prop, None)):
            roots.add(s)
            roots.add(o)
    
    # Remove nodes that have parents
    non_roots = set()
    for s, p, o in graph.triples((None, prop, None)):
        if s in roots:
            non_roots.add(s)
            
    # Return only nodes that don't have parents
    return roots - non_roots