def get_cookies(self, response):
    """
        Gets the cookies from the specified response,and save it to cookies_file.
        :param response: The response to get cookies from, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """
    if isinstance(response, dict) and 'cookies' in response:
        self.cookies = response['cookies']
        self._save_cookies()
    else:
        self.cookies = {}