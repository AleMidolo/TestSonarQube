def load_cookies(self):
    """
        कुकीज़ को cookies_file से कुकीज़ डेटा में लोड करता है।
        :return: कुकीज़ डेटा, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
    try:
        with open(self.cookies_file, 'r') as file:
            self.cookies = json.load(file)
        return self.cookies
    except (FileNotFoundError, json.JSONDecodeError):
        return {}