from typing import Optional, Set

def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    all_nodes = {s for s, p, o in graph}  # Get all subjects in the graph
    child_nodes = {o for s, p, o in graph if p == prop}  # Get all child nodes

    # Find root nodes (nodes that are not children of any node)
    root_nodes = all_nodes - child_nodes

    return root_nodes