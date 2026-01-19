def get_scheme(self):
    """
    URL का स्कीम प्राप्त करें
    :return: स्ट्रिंग, यदि सफल हो, तो URL का स्कीम लौटाएं
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_scheme()
    "https"
    """
    from urllib.parse import urlparse
    parsed_url = urlparse(self.url)
    return parsed_url.scheme