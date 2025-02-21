def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento NodeInfo `.well-known`.

    Consulta la specifica: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)

    :param url: L'URL base completo con protocollo, ad esempio `https://example.com`  
    :param document_path: Percorso personalizzato per il documento NodeInfo, se fornito (opzionale)  
    :returns: dict
    """
    import json

    nodeinfo_document = {
        "version": "2.0",
        "links": [
            {
                "rel": "self",
                "href": f"{url}/{document_path or '.well-known/nodeinfo'}"
            },
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}/{document_path or '.well-known/nodeinfo'}/2.0"
            }
        ]
    }

    return nodeinfo_document