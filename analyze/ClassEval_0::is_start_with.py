def is_start_with(self, request_uri):
    """
        Controlla se l'URI della richiesta inizia con determinati prefissi.
        Attualmente, i prefissi controllati sono "/api" e "/login".
        :param request_uri: str, l'URI della richiesta
        :return: bool, True se l'URI inizia con determinati prefissi, False altrimenti
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True
        """
    return request_uri.startswith(('/api', '/login'))