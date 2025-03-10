def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming RequestType has a 'headers' attribute that is a dictionary
    if hasattr(request, 'headers'):
        # Check for a common Matrix header, e.g., 'Authorization: Bearer' or 'Content-Type: application/json'
        if 'Authorization' in request.headers and request.headers['Authorization'].startswith('Bearer '):
            return True
        if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
            return True
    return False