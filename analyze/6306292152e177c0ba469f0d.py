def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    """
    # Check if request is None
    if request is None:
        return False
        
    # Check if request has Matrix-specific headers
    headers = request.headers if hasattr(request, 'headers') else {}
    
    # Look for common Matrix protocol identifiers in headers
    matrix_headers = [
        'Authorization',  # Matrix uses Bearer tokens
        'X-Matrix',      # Custom Matrix header
        'Origin'         # Check for Matrix homeserver origin
    ]
    
    for header in matrix_headers:
        if header in headers:
            # If Authorization header exists, check if it's a Matrix bearer token
            if header == 'Authorization':
                auth_value = headers[header]
                if auth_value.startswith('Bearer') and '_matrix_' in auth_value:
                    return True
            # If other Matrix headers exist
            else:
                return True
                
    # Check URL path for Matrix endpoints
    path = request.path if hasattr(request, 'path') else ''
    matrix_endpoints = ['/_matrix/', '/matrix/', '/_synapse/']
    
    return any(endpoint in path for endpoint in matrix_endpoints)