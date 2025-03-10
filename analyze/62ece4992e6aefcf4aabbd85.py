from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
    """
    Trova le radici in una sorta di gerarchia transitiva.

    find_roots(graph, rdflib.RDFS.subClassOf)

    restituirà un insieme contenente tutte le radici della gerarchia delle sottoclassi.

    Presuppone triple nella forma (figlio, prop, genitore), ovvero la direzione di
    `RDFS.subClassOf` o `SKOS.broader`.
    """
    if roots is None:
        roots = set()

    # Trova tutti i nodi che non hanno genitori rispetto alla proprietà `prop`
    for child, _, _ in graph.triples((None, prop, None)):
        if child not in roots:
            roots.add(child)

    # Rimuovi i nodi che hanno genitori
    for child, _, parent in graph.triples((None, prop, None)):
        if parent in roots:
            roots.discard(parent)

    return roots