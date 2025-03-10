from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    """
    Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader
    """
    if roots is None:
        roots = set()

    # Get all nodes that appear as children in the graph
    children = set(graph.subjects(prop, None))

    # Get all nodes that appear as parents in the graph
    parents = set(graph.objects(None, prop))

    # Roots are nodes that are parents but not children
    roots.update(parents - children)

    return roots