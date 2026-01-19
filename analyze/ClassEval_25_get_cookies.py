def get_cookies(self, response):
    """
    Obtiene las cookies de la respuesta especificada y las guarda en cookies_file.
    :param reponse: La respuesta de la que obtener las cookies, dict.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
    >>> cookies_util.cookies
    {'key1': 'value1', 'key2': 'value2'}

    """
    self.cookies = response.get('cookies', {})
    self._save_cookies()