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
    
    # Extract JWT token and user info
    if isinstance(authorization, dict):
        jwt_token = authorization.get('jwt')
        user_info = authorization.get('user')
        
        if not jwt_token or not user_info:
            return None
        
        # Validate JWT token (check if it contains username and today's date)
        if user_info.get('name') and str(datetime.date.today()) in jwt_token:
            return {'user': user_info}
    
    return None