from typing import Optional, Set

def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()
    
    all_nodes = {s for s, p, o in graph.triples((None, prop, None))}
    child_nodes = {o for s, p, o in graph.triples((None, prop, None))}
    
    for node in child_nodes:
        if node not in all_nodes:
            roots.add(node)
    
    return roots