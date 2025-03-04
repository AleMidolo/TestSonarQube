def find_roots(graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None) -> Set["Node"]:
    # If roots not provided, get all subjects that appear as objects in prop relationships
    if roots is None:
        roots = set()
        for s, p, o in graph.triples((None, prop, None)):
            roots.add(s)
            roots.add(o)
    
    # For each root candidate, check if it has any parents
    # If it has parents, remove it from roots
    to_remove = set()
    for node in roots:
        for _, _, parent in graph.triples((node, prop, None)):
            to_remove.add(node)
            break
            
    # Remove non-root nodes
    roots.difference_update(to_remove)
    
    return roots