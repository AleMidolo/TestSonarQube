def is_start_with(self, request_uri):
    """
        检查请求 URI 是否以某些前缀开头。
        当前检查的前缀是 "/api" 和 "/login"。
        :param request_uri: str，请求的 URI
        :return: bool，如果 URI 以某些前缀开头则返回 True，否则返回 False
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        """
    return request_uri.startswith('/api') or request_uri.startswith('/login')