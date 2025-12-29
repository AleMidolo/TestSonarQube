def filter(self, request):
    """
        Filtra la richiesta in arrivo in base a determinate regole e condizioni.
        :param request: dict, i dettagli della richiesta in arrivo
        :return: bool, True se la richiesta è consentita, False altrimenti
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True
        """
    if self.is_start_with(request['path']):
        return True
    return False