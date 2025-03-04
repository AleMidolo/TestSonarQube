def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # Initialize empty set if roots not provided
    if roots is None:
        roots = set()
        
    # Get all subjects and objects connected by the property
    subjects = set(graph.subjects(prop))
    objects = set(graph.objects(prop))
    
    # Root nodes are subjects that are not objects
    root_nodes = subjects - objects
    
    # If no roots found and we have subjects, pick arbitrary subject as root
    if not root_nodes and subjects:
        root_nodes = {next(iter(subjects))}
        
    # Add found roots to provided/initialized set
    roots.update(root_nodes)
    
    return roots