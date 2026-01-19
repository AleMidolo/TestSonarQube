def load_cookies(self):
    """
    从 cookies_file 加载 cookies 到 cookies 数据中。
    :return: cookies 数据，dict。
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.load_cookies()
    {'key1': 'value1', 'key2': 'value2'}

    """
    import json
    import os
    
    if not hasattr(self, 'cookies_file'):
        return {}
    
    if not os.path.exists(self.cookies_file):
        return {}
    
    try:
        with open(self.cookies_file, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
            if isinstance(cookies, dict):
                return cookies
            else:
                return {}
    except (json.JSONDecodeError, IOError):
        return {}