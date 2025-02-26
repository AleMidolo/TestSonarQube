from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    """
    Encuentra las raíces en algún tipo de jerarquía transitiva.

    find_roots(graph, rdflib.RDFS.subClassOf)

    Devolverá un conjunto con todas las raíces de la jerarquía de subclases.

    Se asume que los triples tienen la forma `(hijo, prop, padre)`, es decir, la dirección de `RDFS.subClassOf` o `SKOS.broader`.

    Argumentos:
    graph: Objeto de la clase `Graph`.
    prop: Objeto de la clase `URIRef`.
    roots: Lista opcional con tipo `set`.

    Retorno:
    roots: Un conjunto con los nodos.
    """
    if roots is None:
        roots = set()

    # Encuentra todos los nodos que tienen un padre
    children = {s for s, p, o in graph.triples((None, prop, None))}

    # Encuentra todos los nodos que son padres
    parents = {o for s, p, o in graph.triples((None, prop, None))}

    # Las raíces son aquellos nodos que no tienen padres
    roots = children - parents

    return roots