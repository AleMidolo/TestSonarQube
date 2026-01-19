def get_jwt_user(self, request):
    """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}}
        """
    auth_header = request.get('headers', {}).get('Authorization', {})
    if 'jwt' in auth_header:
        return auth_header['user']
    return None