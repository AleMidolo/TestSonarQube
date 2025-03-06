from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
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

    # If no candidates, return the current roots
    if not candidates:
        return roots

    # Find nodes that are not objects of any triple with the given property
    new_roots = set()
    for candidate in candidates:
        if not any(triple for triple in graph.triples((None, prop, candidate))):
            new_roots.add(candidate)

    # Add new roots to the result set
    roots.update(new_roots)

    # Recursively find roots for the remaining candidates
    remaining_candidates = candidates - new_roots
    if remaining_candidates:
        return find_roots(graph, prop, roots)

    return roots