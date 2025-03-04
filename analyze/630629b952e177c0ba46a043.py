def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento .well-known de NodeInfo.

    Consulta la especificación: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)

    :arg url: La URL base completa con protocolo, por ejemplo, `https://example.com`.
    :arg document_path: Ruta personalizada para el documento NodeInfo si se proporciona (opcional).

    :returns:
    Un diccionario (`dict`).
    """
    # Si no se proporciona una ruta personalizada, usar la ruta por defecto
    if document_path is None:
        document_path = "/nodeinfo/2.0"

    # Asegurarse de que la URL no termine en /
    url = url.rstrip('/')
    
    # Asegurarse de que document_path comience con /
    if not document_path.startswith('/'):
        document_path = '/' + document_path

    # Crear el documento well-known según la especificación
    well_known_document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}{document_path}"
            }
        ]
    }

    return well_known_document