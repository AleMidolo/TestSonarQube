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
        'Authorization',  # Matrix uses bearer tokens
        'X-Matrix',      # Custom Matrix header
        'Origin'         # Check for Matrix homeserver origin
    ]
    
    for header in matrix_headers:
        if header in headers:
            # If authorization header exists, check if it starts with 'Bearer'
            if header == 'Authorization' and headers[header].startswith('Bearer'):
                return True
            # If X-Matrix header exists
            elif header == 'X-Matrix':
                return True
            # If Origin matches Matrix homeserver pattern
            elif header == 'Origin' and 'matrix' in headers[header].lower():
                return True
                
    # Check URL path if available
    if hasattr(request, 'path'):
        matrix_paths = ['/_matrix', '/_synapse', '/_client']
        return any(path in request.path for path in matrix_paths)
        
    return False