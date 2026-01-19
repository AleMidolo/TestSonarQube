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
    
    if not hasattr(self, 'cookie_file'):
        return {}
    
    if not os.path.exists(self.cookie_file):
        return {}
    
    try:
        with open(self.cookie_file, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
            return cookies if isinstance(cookies, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}