def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Check if request has Matrix-specific headers
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        if auth_header.startswith('Bearer'):
            # Matrix access tokens are typically Bearer tokens
            return True
            
    # Check for Matrix API endpoints in request path
    matrix_endpoints = ['/_matrix', '/_synapse']
    for endpoint in matrix_endpoints:
        if request.path.startswith(endpoint):
            return True
            
    # Check content type for Matrix-specific formats
    if 'Content-Type' in request.headers:
        content_type = request.headers['Content-Type']
        if 'application/json' in content_type and any(x in request.path for x in ['sync', 'events', 'rooms']):
            return True
            
    return False