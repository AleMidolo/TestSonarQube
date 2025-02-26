from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    # Get all subjects and objects for the given property
    children = set(graph.subjects(prop))
    parents = set(graph.objects(None, prop))

    # Find roots by checking which children have no parents
    for child in children:
        if child not in parents:
            roots.add(child)

    return roots