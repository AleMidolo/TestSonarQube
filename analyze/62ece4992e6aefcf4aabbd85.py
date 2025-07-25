from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
    """
    यह फ़ंक्शन ट्रांजिटिव पदानुक्रम में रूट्स खोजने के लिए उपयोग किया जाता है। उदाहरण के लिए, यदि आप `graph` और `rdflib.RDFS.subClassOf` पास करते हैं, तो यह उप-वर्ग पदानुक्रम के सभी रूट्स का सेट लौटाएगा।
    """
    if roots is None:
        roots = set()
    
    # Collect all nodes that are subjects in the graph with the given property
    all_nodes = set(graph.subjects(prop, None))
    
    # Find nodes that are not objects in any triple with the given property
    for node in all_nodes:
        if not any(graph.triples((None, prop, node))):
            roots.add(node)
    
    return roots