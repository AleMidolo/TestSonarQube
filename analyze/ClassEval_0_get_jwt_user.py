def get_jwt_user(self, request):
    """
    Get the user information from the JWT token in the request.
    :param request: dict, the incoming request details
    :return: dict or None, the user information if the token is valid, None otherwise
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    import datetime
    
    if not request or 'headers' not in request:
        return None
    
    headers = request.get('headers', {})
    authorization = headers.get('Authorization')
    
    if not authorization:
        return None
    
    # Check if authorization is a dict with 'user' and 'jwt' keys
    if isinstance(authorization, dict):
        user_info = authorization.get('user')
        jwt_token = authorization.get('jwt')
        
        if not user_info or not jwt_token:
            return None
        
        # Validate JWT token (simple validation based on the doctest pattern)
        # The token should contain username + today's date
        if user_info and 'name' in user_info:
            expected_token = user_info['name'] + str(datetime.date.today())
            if jwt_token == expected_token:
                return {'user': user_info}
    
    return None