def get_host(self):
    """
    获取 URL 的第二部分，即主机域名
    :return: 字符串，如果成功，返回 URL 的主机域名
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_host()
    "www.baidu.com"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    return parsed_url.netloc