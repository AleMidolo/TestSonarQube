def _save_cookies(self):
    """
    कुकीज़ को cookies_file में सहेजता है, और यदि सफल होता है तो True लौटाता है, अन्यथा False।
    :return: यदि सफल हो तो True, अन्यथा False।
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
    >>> cookies_util._save_cookies()
    True

    """
    try:
        import json
        with open(self.cookies_file, 'w', encoding='utf-8') as f:
            json.dump(self.cookies, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False