from typing import Optional, Set

def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()
    
    all_nodes = {s for s, p, o in graph}
    child_nodes = {o for s, p, o in graph if p == prop}
    
    root_candidates = all_nodes - child_nodes
    roots.update(root_candidates)
    
    return roots