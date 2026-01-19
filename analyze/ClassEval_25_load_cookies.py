def load_cookies(self):
    """
    Carica i cookie dal file dei cookie nel dato dei cookie.
    :return: I dati dei cookie, dict.
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.load_cookies()
    {'key1': 'value1', 'key2': 'value2'}

    """
    import json
    import os
    
    try:
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'r', encoding='utf-8') as f:
                cookies_data = json.load(f)
                return cookies_data if isinstance(cookies_data, dict) else {}
        else:
            return {}
    except (json.JSONDecodeError, IOError):
        return {}