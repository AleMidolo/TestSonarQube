def find_roots(graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None) -> Set["Node"]:
    # Initialize roots set if not provided
    if roots is None:
        # Get all subjects that appear as objects in triples with the given property
        children = {s for s in graph.subjects(prop)}
        # Get all objects that appear in triples with the given property 
        parents = {o for o in graph.objects(None, prop)}
        # Roots are parents that are not children
        roots = parents - children
        
    # If no roots found, get all subjects that have the property
    if not roots:
        roots = {s for s in graph.subjects(prop)}
        
    return roots