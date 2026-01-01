def get_jwt_user(self, request):
    """
        从请求中的JWT令牌获取用户信息。
        :param request: dict，传入的请求详情
        :return: dict或None，如果令牌有效则返回用户信息，否则返回None
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