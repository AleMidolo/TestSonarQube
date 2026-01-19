def get_cookies(self, reponse):
    """
    Gets the cookies from the specified response,and save it to cookies_file.
    :param reponse: The response to get cookies from, dict.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
    >>> cookies_util.cookies
    {'key1': 'value1', 'key2': 'value2'}

    """
    if 'cookies' in reponse:
        self.cookies = reponse['cookies']
        self._save_cookies()