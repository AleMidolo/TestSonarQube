def _save_cookies(self):
    """
    Salva i cookie nel file cookies_file e restituisce True se ha successo, False altrimenti.
    :return: True se ha successo, False altrimenti.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
    >>> cookies_util._save_cookies()
    True

    """
    try:
        import json
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f)
        return True
    except Exception:
        return False