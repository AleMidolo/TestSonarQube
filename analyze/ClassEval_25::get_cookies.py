def get_cookies(self, response):
    """
        从指定的响应中获取 cookies，并将其保存到 cookies_file。
        :param response: 要从中获取 cookies 的响应，dict。
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