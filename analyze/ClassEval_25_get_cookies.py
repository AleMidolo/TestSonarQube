def get_cookies(self, reponse):
    """
    Obtiene las cookies de la respuesta especificada y las guarda en cookies_file.
    :param reponse: La respuesta de la que obtener las cookies, dict.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
    >>> cookies_util.cookies
    {'key1': 'value1', 'key2': 'value2'}

    """
    if 'cookies' in reponse:
        self.cookies = reponse['cookies']
        # Save cookies to file
        import json
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f)