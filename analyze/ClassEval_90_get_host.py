def get_host(self):
    """
    Get the second part of the URL, which is the host domain name
    :return: string, If successful, return the host domain name of the URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_host()
    "www.baidu.com"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    return parsed_url.netloc