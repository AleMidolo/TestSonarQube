def filter(self, request):
    """
        Filtra la richiesta in arrivo in base a determinate regole e condizioni.
        :param request: dict, i dettagli della richiesta in arrivo
        :return: bool, True se la richiesta è consentita, False altrimenti
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
    if not self.is_start_with(request.get('path', '')):
        return False
    if request.get('path', '').startswith('/api'):
        headers = request.get('headers', {})
        if 'Authorization' not in headers:
            return False
        user_info = self.get_jwt_user(request)
        if user_info is None:
            return False
        self.set_current_user_info_and_log(user_info.get('user', {}))
    return True