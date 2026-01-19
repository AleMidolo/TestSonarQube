def set_current_user_info_and_log(self, user):
    """
    设置当前用户信息并记录访问日志。
    :param user: dict，用户信息
    :return: None
    >>> filter = AccessGatewayFilter()
    >>> user = {'name': 'user1', 'address': '127.0.0.1'}
    >>> filter.set_current_user_info_and_log(user)

    """
    self.current_user = user
    
    user_name = user.get('name', 'Unknown')
    user_address = user.get('address', 'Unknown')
    
    log_message = f"User '{user_name}' accessed from address '{user_address}'"
    
    if not hasattr(self, 'access_logs'):
        self.access_logs = []
    
    self.access_logs.append(log_message)
    
    print(log_message)