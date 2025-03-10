import json
from urllib.parse import urljoin

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento NodeInfo `.well-known`.

    Consulta la specifica: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)

    :param url: L'URL base completo con protocollo, ad esempio `https://example.com`  
    :param document_path: Percorso personalizzato per il documento NodeInfo, se fornito (opzionale)  
    :returns: dict
    """
    if document_path is None:
        document_path = "/.well-known/nodeinfo"
    
    well_known_url = urljoin(url, document_path)
    
    # Simulazione di un documento NodeInfo ben noto
    nodeinfo_document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": urljoin(url, "/nodeinfo/2.0")
            }
        ]
    }
    
    return nodeinfo_document