def set_current_user_info_and_log(self, user):
    """
    वर्तमान उपयोगकर्ता की जानकारी सेट करें और पहुंच को लॉग करें।
    :param user: dict, उपयोगकर्ता की जानकारी
    :return: None
    >>> filter = AccessGatewayFilter()
    >>> user = {'name': 'user1', 'address': '127.0.0.1'}
    >>> filter.set_current_user_info_and_log(user)

    """
    self.current_user_info = user
    print(f"User {user.get('name')} logged in from {user.get('address')}")