from typing import Optional, Set

def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()
    
    # Trova tutti i nodi che non hanno genitori
    all_children = {s for s, p, o in graph.triples((None, prop, None))}
    all_parents = {o for s, p, o in graph.triples((None, prop, None))}
    
    # Le radici sono i nodi che non sono genitori di nessun altro nodo
    roots = all_children - all_parents
    
    return roots