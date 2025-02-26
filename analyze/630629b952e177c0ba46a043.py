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
        "services": {
            "outbound": [],
            "inbound": []
        },
        "metadata": {
            "name": "Example Node",
            "description": "An example NodeInfo document",
            "url": url,
            "version": "1.0"
        }
    }

    if document_path:
        nodeinfo_url = f"{url}/{document_path}"
    else:
        nodeinfo_url = f"{url}/.well-known/nodeinfo"

    return {
        "nodeinfo_url": nodeinfo_url,
        "document": nodeinfo_document
    }