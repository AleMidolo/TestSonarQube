def get_host(self):
    """
    URL का दूसरा भाग प्राप्त करें, जो होस्ट डोमेन नाम है
    :return: स्ट्रिंग, यदि सफल हो, तो URL का होस्ट डोमेन नाम लौटाएं
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_host()
    "www.baidu.com"
    """
    from urllib.parse import urlparse
    parsed_url = urlparse(self.url)
    return parsed_url.netloc