def load_cookies(self):
    """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
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