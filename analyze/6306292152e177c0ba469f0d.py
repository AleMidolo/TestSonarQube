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
            
    # Check for Matrix API endpoints
    if request.path.startswith('/_matrix/'):
        return True
        
    # Check for Matrix server name in host header
    if 'Host' in request.headers:
        host = request.headers['Host']
        if '.matrix.' in host or host.endswith('.matrix'):
            return True
            
    # Check content type for Matrix-specific formats
    if 'Content-Type' in request.headers:
        content_type = request.headers['Content-Type']
        if 'application/json' in content_type and request.json:
            # Look for Matrix event types in JSON body
            if 'm.room.' in str(request.json) or 'm.presence' in str(request.json):
                return True
                
    return False