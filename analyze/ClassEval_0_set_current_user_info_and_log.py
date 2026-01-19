def set_current_user_info_and_log(self, user):
    """
    Imposta le informazioni dell'utente corrente e registra l'accesso.
    :param user: dict, le informazioni dell'utente
    :return: None
    >>> filter = AccessGatewayFilter()
    >>> user = {'name': 'user1', 'address': '127.0.0.1'}
    >>> filter.set_current_user_info_and_log(user)

    """
    self.current_user_info = user
    self.log_access(user)