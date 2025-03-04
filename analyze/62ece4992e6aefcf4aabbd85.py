from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    # Get all nodes that have no parents
    all_children = {s for s, p, o in graph.triples((None, prop, None))}
    all_parents = {o for s, p, o in graph.triples((None, prop, None))}

    # Roots are those nodes that are not parents of any other nodes
    roots = all_children - all_parents

    return roots