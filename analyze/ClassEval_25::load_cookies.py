def load_cookies(self):
    """
        Carga las cookies del archivo de cookies.
        :return: Los datos de las cookies, dict.
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