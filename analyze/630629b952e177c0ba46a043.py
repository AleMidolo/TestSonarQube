import json
from urllib.parse import urljoin

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento .well-known de NodeInfo.

    Consulta la especificación: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)

    :arg url: La URL base completa con protocolo, por ejemplo, `https://example.com`.
    :arg document_path: Ruta personalizada para el documento NodeInfo si se proporciona (opcional).

    :returns:
    Un diccionario (`dict`).
    """
    if document_path is None:
        document_path = ".well-known/nodeinfo"
    
    nodeinfo_url = urljoin(url, document_path)
    
    well_known_document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": urljoin(nodeinfo_url, "nodeinfo/2.0")
            },
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
                "href": urljoin(nodeinfo_url, "nodeinfo/2.1")
            }
        ]
    }
    
    return well_known_document