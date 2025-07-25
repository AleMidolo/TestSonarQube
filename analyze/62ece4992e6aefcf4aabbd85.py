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

    # Trova tutti i nodi che sono figli nella gerarchia
    children = set(graph.subjects(prop, None))

    # Trova tutti i nodi che sono genitori nella gerarchia
    parents = set(graph.objects(None, prop))

    # Le radici sono i nodi che non sono figli di nessun altro nodo
    roots.update(parents - children)

    return roots