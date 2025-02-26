from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    # Collect all nodes that have children
    children = {s for s, p, o in graph.triples((None, prop, None))}

    # Collect all nodes that are not children of any node
    all_nodes = {s for s, p, o in graph.triples((None, None, None))}
    roots = all_nodes - children

    return roots