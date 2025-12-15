def load_cookies(self):
        """
        从 cookies_file 加载 cookies 到 cookies 数据中。
        :return: cookies 数据，dict。
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