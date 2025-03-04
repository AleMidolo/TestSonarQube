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
        'Matrix-'        # Matrix protocol prefix
    ]
    
    for header in matrix_headers:
        if any(h.startswith(header) for h in headers.keys()):
            return True
            
    # Check URL path if available
    path = request.path if hasattr(request, 'path') else ''
    matrix_paths = ['/_matrix/', '/_synapse/']
    
    if any(p in path for p in matrix_paths):
        return True
        
    return False