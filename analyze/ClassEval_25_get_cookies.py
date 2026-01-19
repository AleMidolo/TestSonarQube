def get_cookies(self, reponse):
    """
    Ottiene i cookie dalla risposta specificata e li salva nel file cookies_file.
    :param reponse: La risposta da cui ottenere i cookie, dict.
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