def get_scheme(self):
    """
    获取URL的协议
    :return: 字符串，如果成功，返回URL的协议
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_scheme()
    "https"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    return parsed_url.scheme