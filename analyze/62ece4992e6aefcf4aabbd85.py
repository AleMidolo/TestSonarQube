def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()
    
    for node in graph.subjects(prop, None):
        roots.add(node)
        find_roots(graph, prop, roots)
    
    return roots