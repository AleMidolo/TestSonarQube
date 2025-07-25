from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    if roots is None:
        roots = set()
    
    # Find all nodes that are subjects of the property
    subjects = set(graph.subjects(prop, None))
    
    # Find all nodes that are objects of the property
    objects = set(graph.objects(None, prop))
    
    # Roots are subjects that are not objects
    roots.update(subjects - objects)
    
    return roots