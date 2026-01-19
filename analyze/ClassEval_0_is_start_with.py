def is_start_with(self, request_uri):
    """
        Verifica si la URI de la solicitud comienza con ciertos prefijos.
        Actualmente, los prefijos que se están verificando son "/api" y "/login".
        :param request_uri: str, la URI de la solicitud
        :return: bool, True si la URI comienza con ciertos prefijos, False en caso contrario
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        """
    return request_uri.startswith('/api') or request_uri.startswith('/login')