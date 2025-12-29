def get_jwt_user(self, request):
    """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}}
        """
    try:
        auth_header = request.get('headers', {}).get('Authorization', {})
        jwt_token = auth_header.get('jwt', '')
        expected_token = auth_header.get('user', {}).get('name', '') + str(datetime.date.today())
        if jwt_token == expected_token:
            return {'user': auth_header.get('user', {})}
        else:
            return None
    except:
        return None