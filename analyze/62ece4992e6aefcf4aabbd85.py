from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    # Get all nodes that have no parents
    all_nodes = set(graph.subjects())
    child_nodes = set(graph.objects(None, prop))
    root_candidates = all_nodes - child_nodes

    # Add root candidates to the roots set
    roots.update(root_candidates)

    return roots