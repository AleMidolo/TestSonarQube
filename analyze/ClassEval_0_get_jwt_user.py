def get_jwt_user(self, request):
    """
    从请求中的JWT令牌获取用户信息。
    :param request: dict，传入的请求详情
    :return: dict或None，如果令牌有效则返回用户信息，否则返回None
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
    
    # 如果Authorization是字典类型
    if isinstance(authorization, dict):
        jwt_token = authorization.get('jwt')
        user_info = authorization.get('user')
        
        if jwt_token and user_info:
            # 验证JWT令牌（根据示例，令牌格式为 username + 今天的日期）
            username = user_info.get('name', '')
            expected_token = username + str(datetime.date.today())
            
            if jwt_token == expected_token:
                return {'user': user_info}
    
    return None