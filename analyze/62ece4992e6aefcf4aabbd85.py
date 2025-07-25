from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    # Get all nodes that have the property as a child
    children = set(graph.subjects(prop, None))

    # Find all nodes that are not children (i.e., they are roots)
    all_nodes = set(graph.subjects())
    roots = all_nodes - children

    return roots