def load_cookies(self):
    """
        Carica i cookie dal file dei cookie nel dato dei cookie.
        :return: I dati dei cookie, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
    try:
        with open(self.cookies_file, 'r') as file:
            self.cookies = json.load(file)
        return self.cookies
    except (FileNotFoundError, json.JSONDecodeError):
        return None