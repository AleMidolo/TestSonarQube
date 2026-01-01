def filter(self, request):
    """
    根据某些规则和条件过滤传入的请求。
    :param request: dict，传入请求的详细信息
    :return: bool，如果请求被允许则返回 True，否则返回 False
    >>> filter = AccessGatewayFilter()
    >>> filter.filter({'path': '/login', 'method': 'POST'})
    True

    """
    if self.is_start_with(request['path']):
        user_info = self.get_jwt_user(request)
        if user_info:
            self.set_current_user_info_and_log(user_info['user'])
            return True
    return False