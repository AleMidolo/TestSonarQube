def find_roots(graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None) -> Set["Node"]:
    # Initialize roots set if not provided
    if roots is None:
        # Get all subjects that appear as objects in triples with the given property
        children = {s for s in graph.subjects(prop)}
        # Get all objects that appear in triples with the given property 
        parents = {o for o in graph.objects(prop)}
        # Roots are parents that are not children
        roots = parents - children
        
    # If no roots found, return empty set
    if not roots:
        return set()
        
    # Get all subjects that have these roots as objects via the property
    new_roots = set()
    for root in roots:
        new_roots.update(graph.subjects(prop, root))
        
    # Recursively find roots of the new subjects
    if new_roots:
        roots.update(find_roots(graph, prop, new_roots))
        
    return roots