import datetime

def get_jwt_user(self, request):
    """
    从请求中的JWT令牌获取用户信息。
    :param request: dict，传入的请求详情
    :return: dict或None，如果令牌有效则返回用户信息，否则返回None
    >>> filter = AccessGatewayFilter()
    >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
    {'user': {'name': 'user1'}

    """
    try:
        # 从请求中获取headers
        headers = request.get('headers', {})
        
        # 从headers中获取Authorization
        authorization = headers.get('Authorization', {})
        
        # 检查authorization是否为字典类型
        if not isinstance(authorization, dict):
            return None
        
        # 获取JWT令牌和用户信息
        jwt_token = authorization.get('jwt', '')
        user_info = authorization.get('user', {})
        
        # 验证JWT令牌
        # 根据docstring示例，JWT格式为: username + today's date
        if user_info and 'name' in user_info:
            expected_jwt = user_info['name'] + str(datetime.date.today())
            
            # 如果JWT令牌有效，返回用户信息
            if jwt_token == expected_jwt:
                return {'user': user_info}
        
        return None
    except Exception:
        return None