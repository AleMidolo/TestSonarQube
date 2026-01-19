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
        if 'headers' not in request or 'Authorization' not in request['headers']:
            return False
        user_info = self.get_jwt_user(request)
        if user_info is None:
            return False
        if 'user' in user_info and 'address' in request:
            user_with_address = user_info['user'].copy()
            user_with_address['address'] = request.get('address', 'unknown')
            self.set_current_user_info_and_log(user_with_address)
    return True