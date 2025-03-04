def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    # Check if request has Matrix-specific headers or patterns
    if hasattr(request, 'headers'):
        # Look for common Matrix headers
        matrix_headers = [
            'Authorization',
            'X-Matrix',
            'Matrix-',
        ]
        
        for header in matrix_headers:
            if header in request.headers:
                return True
                
    # Check URL path if available
    if hasattr(request, 'path'):
        matrix_paths = [
            '/_matrix',
            '/matrix',
            '/.well-known/matrix'
        ]
        
        for path in matrix_paths:
            if request.path.startswith(path):
                return True
                
    # Check request body if available
    if hasattr(request, 'body'):
        matrix_keywords = [
            'access_token',
            'device_id', 
            'user_id',
            'room_id'
        ]
        
        try:
            body = request.body.decode('utf-8')
            for keyword in matrix_keywords:
                if keyword in body:
                    return True
        except:
            pass
            
    return False