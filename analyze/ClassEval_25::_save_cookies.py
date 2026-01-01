def _save_cookies(self):
    """
        将 cookies 保存到 cookies_file，并在成功时返回 True，否则返回 False。
        :return: 成功时返回 True，否则返回 False。
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