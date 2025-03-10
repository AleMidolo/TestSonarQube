from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    """
    यह फ़ंक्शन ट्रांजिटिव पदानुक्रम में रूट्स खोजने के लिए उपयोग किया जाता है। उदाहरण के लिए, यदि आप `graph` और `rdflib.RDFS.subClassOf` पास करते हैं, तो यह उप-वर्ग पदानुक्रम के सभी रूट्स का सेट लौटाएगा।
    """
    if roots is None:
        roots = set()
    
    # Get all nodes that are subjects in the graph with the given property
    subjects = set(graph.subjects(prop, None))
    
    # Iterate through each subject to find roots
    for subject in subjects:
        # If the subject is not an object in any triple with the given property, it's a root
        if not any(graph.triples((None, prop, subject))):
            roots.add(subject)
    
    return roots