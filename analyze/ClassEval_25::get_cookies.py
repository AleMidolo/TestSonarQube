def get_cookies(self, response):
    """
        Ottiene i cookie dalla risposta specificata e li salva nel file cookies_file.
        :param response: La risposta da cui ottenere i cookie, dict.
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