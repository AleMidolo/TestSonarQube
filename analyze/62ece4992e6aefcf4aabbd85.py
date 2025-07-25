from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    """
    Trova le radici in una sorta di gerarchia transitiva.

    find_roots(graph, rdflib.RDFS.subClassOf)

    restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    if roots is None:
        roots = set()

    # Get all nodes that appear as subjects in the graph
    all_nodes = set(graph.subjects())

    # Iterate through all nodes to find those that are not objects of any triple with the given property
    for node in all_nodes:
        if not any(True for _ in graph.triples((None, prop, node))):
            roots.add(node)

    return roots