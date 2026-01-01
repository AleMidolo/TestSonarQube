def get_cookies(self, reponse):
    """
    निर्दिष्ट प्रतिक्रिया से कुकीज़ प्राप्त करता है, और इसे cookies_file में सहेजता है।
    :param reponse: वह प्रतिक्रिया जिससे कुकीज़ प्राप्त की जानी हैं, dict।
    >>> cookies_util = CookiesUtil('cookies.json')
    >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
    >>> cookies_util.cookies
    {'key1': 'value1', 'key2': 'value2'}

    """
    self.cookies = reponse.get('cookies', {})
    self._save_cookies()