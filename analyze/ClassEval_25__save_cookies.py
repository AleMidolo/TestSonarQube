def _save_cookies(self):
    """
        Guarda las cookies en el archivo cookies_file y devuelve True si tiene éxito, False en caso contrario.
        :return: True si tiene éxito, False en caso contrario.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """
    try:
        with open(self.cookies_file, 'w') as file:
            json.dump(self.cookies, file)
        return True
    except Exception:
        return False