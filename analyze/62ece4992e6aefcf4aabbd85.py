from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
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

    # Obtener todos los sujetos que son hijos en la jerarquía
    children = set(graph.subjects(predicate=prop))

    # Obtener todos los objetos que son padres en la jerarquía
    parents = set(graph.objects(predicate=prop))

    # Las raíces son los padres que no son hijos
    roots.update(parents - children)

    return roots