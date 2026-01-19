def set_current_user_info_and_log(self, user):
    """
    Establece la información del usuario actual y registra el acceso.
    :param user: dict, la información del usuario
    :return: None
    >>> filter = AccessGatewayFilter()
    >>> user = {'name': 'user1', 'address': '127.0.0.1'}
    >>> filter.set_current_user_info_and_log(user)

    """
    self.current_user_info = user
    self.log_access(user)