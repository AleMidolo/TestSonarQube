def is_start_with(self, request_uri):
    """
    Check if the request URI starts with certain prefixes.
    Currently, the prefixes being checked are "/api" and "/login".
    :param request_uri: str, the URI of the request
    :return: bool, True if the URI starts with certain prefixes, False otherwise
    >>> filter = AccessGatewayFilter()
    >>> filter.is_start_with('/api/data')
    True

    """
    prefixes = ["/api", "/login"]
    return any(request_uri.startswith(prefix) for prefix in prefixes)