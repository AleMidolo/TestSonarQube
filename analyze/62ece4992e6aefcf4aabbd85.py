def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # Initialize empty set if roots not provided
    if roots is None:
        roots = set()
        
    # Get all subjects and objects connected by the property
    subjects = set(graph.subjects(prop))
    objects = set(graph.objects(prop))
    
    # Root nodes are subjects that are not objects of the property
    root_nodes = subjects - objects
    
    # If roots set was provided, only keep nodes from that set
    if roots:
        root_nodes = root_nodes & roots
        
    return root_nodes