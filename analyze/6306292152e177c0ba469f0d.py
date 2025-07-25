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
        
    # Check for Matrix server name in host
    if request.host and '.matrix.' in request.host:
        return True
        
    # Check content type for Matrix-specific formats
    if request.content_type == 'application/json':
        try:
            body = request.get_json()
            # Check for common Matrix request fields
            if any(key in body for key in ['room_id', 'event_id', 'user_id', 'device_id']):
                return True
        except:
            pass
            
    return False