def load_cookies(self):
    """
    Carga las cookies del archivo de cookies.
    :return: Los datos de las cookies, dict.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.load_cookies()
    {'key1': 'value1', 'key2': 'value2'}

    """
    import json
    import os
    
    try:
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'r', encoding='utf-8') as f:
                cookies = json.load(f)
                return cookies if isinstance(cookies, dict) else {}
        else:
            return {}
    except (json.JSONDecodeError, IOError):
        return {}