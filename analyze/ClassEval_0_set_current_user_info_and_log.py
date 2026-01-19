def set_current_user_info_and_log(self, user):
    """
    Set the current user information and log the access.
    :param user: dict, the user information
    :return: None
    >>> filter = AccessGatewayFilter()
    >>> user = {'name': 'user1', 'address': '127.0.0.1'}
    >>> filter.set_current_user_info_and_log(user)

    """
    self.current_user = user
    self.log_access(user)