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
        with open(self.cookies_file, 'w') as file:
            json.dump(self.cookies, file)
        return True
    except Exception:
        return False