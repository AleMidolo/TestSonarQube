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
    
    # Use default nodeinfo path if none provided
    if document_path is None:
        document_path = '/nodeinfo/2.0'
    else:
        # Ensure document path starts with slash
        document_path = f'/{document_path.lstrip("/")}'
        
    # Build well-known document
    well_known = {
        'links': [
            {
                'rel': 'http://nodeinfo.diaspora.software/ns/schema/2.0',
                'href': f'{url}{document_path}'
            }
        ]
    }
    
    return well_known