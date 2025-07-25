import json

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
    
    nodeinfo_url = f"{url}{document_path}"
    
    well_known_document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}/nodeinfo/2.0"
            },
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
                "href": f"{url}/nodeinfo/2.1"
            }
        ]
    }
    
    return well_known_document