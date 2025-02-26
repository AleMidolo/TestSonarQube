from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    all_nodes = set(graph.subjects(prop, None))
    child_nodes = set(graph.objects(None, prop))

    for node in all_nodes:
        if node not in child_nodes:
            roots.add(node)

    return roots