def load_cookies(self):
    """
    कुकीज़ को cookies_file से कुकीज़ डेटा में लोड करता है।
    :return: कुकीज़ डेटा, dict.
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
            cookies_data = json.load(f)
            return cookies_data if isinstance(cookies_data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}