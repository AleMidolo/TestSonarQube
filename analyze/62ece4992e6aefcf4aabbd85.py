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

    # Obtener todos los nodos que son sujetos en triples con la propiedad dada
    subjects = set(graph.subjects(predicate=prop))

    # Obtener todos los nodos que son objetos en triples con la propiedad dada
    objects = set(graph.objects(predicate=prop))

    # Las raíces son los nodos que son sujetos pero no objetos
    roots.update(subjects - objects)

    return roots