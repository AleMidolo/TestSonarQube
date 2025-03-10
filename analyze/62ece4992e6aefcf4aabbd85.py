from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    """
    यह फ़ंक्शन ट्रांजिटिव पदानुक्रम में रूट्स खोजने के लिए उपयोग किया जाता है। उदाहरण के लिए, यदि आप `graph` और `rdflib.RDFS.subClassOf` पास करते हैं, तो यह उप-वर्ग पदानुक्रम के सभी रूट्स का सेट लौटाएगा।
    """
    if roots is None:
        roots = set()
    
    # Find all nodes that are subjects of the property
    subjects = set(graph.subjects(prop))
    
    # Find all nodes that are objects of the property
    objects = set(graph.objects(None, prop))
    
    # Roots are subjects that are not objects
    roots.update(subjects - objects)
    
    return roots