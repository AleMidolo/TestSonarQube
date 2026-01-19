def get_cookies(self, reponse):
    """
    从指定的响应中获取 cookies，并将其保存到 cookies_file。
    :param reponse: 要从中获取 cookies 的响应，dict。
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
    >>> cookies_util.cookies
    {'key1': 'value1', 'key2': 'value2'}
    """
    if 'cookies' in reponse:
        self.cookies = reponse['cookies']
        self.save_cookies()