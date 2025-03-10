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
    
    # Get all nodes that appear as subjects in the graph with the given property
    candidates = set(graph.subjects(predicate=prop))
    
    # Get all nodes that appear as objects in the graph with the given property
    parents = set(graph.objects(predicate=prop))
    
    # Roots are candidates that are not in parents
    roots.update(candidates - parents)
    
    return roots