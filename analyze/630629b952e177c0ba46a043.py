import json

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento .well-known de NodeInfo.

    Consulta la especificación: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)

    :arg url: La URL base completa con protocolo, por ejemplo, `https://example.com`.
    :arg document_path: Ruta personalizada para el documento NodeInfo si se proporciona (opcional).

    :returns:
    Un diccionario (`dict`).
    """
    if document_path:
        nodeinfo_url = f"{url}/{document_path.lstrip('/')}"
    else:
        nodeinfo_url = f"{url}/.well-known/nodeinfo"

    document = {
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

    return document