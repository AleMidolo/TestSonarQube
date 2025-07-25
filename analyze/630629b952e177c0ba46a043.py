def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Genera un documento NodeInfo `.well-known`.
    
    Consulta la specifica: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)
    
    :param url: L'URL base completo con protocollo, ad esempio `https://example.com`  
    :param document_path: Percorso personalizzato per il documento NodeInfo, se fornito (opzionale)  
    :returns: dict
    """
    # Remove trailing slash from url if present
    url = url.rstrip('/')
    
    # Use default path if none provided
    if document_path is None:
        document_path = '/nodeinfo/2.0'
        
    # Remove leading slash from document path if present
    document_path = document_path.lstrip('/')
    
    # Build the full nodeinfo URL
    nodeinfo_url = f"{url}/{document_path}"
    
    # Create the well-known document according to spec
    well_known = {
        'links': [
            {
                'rel': 'http://nodeinfo.diaspora.software/ns/schema/2.0',
                'href': nodeinfo_url
            }
        ]
    }
    
    return well_known