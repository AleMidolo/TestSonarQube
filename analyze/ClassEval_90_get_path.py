def get_path(self):
    """
    获取 URL 的第三部分，即资源的地址
    :return: 字符串，如果成功，返回 URL 的资源地址
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_path()
    "/s?wd=aaa&rsv_spt=1#page"
    """
    from urllib.parse import urlparse
    
    parsed = urlparse(self.url)
    path = parsed.path
    
    # Add query string if present
    if parsed.query:
        path += '?' + parsed.query
    
    # Add fragment if present
    if parsed.fragment:
        path += '#' + parsed.fragment
    
    return path if path else "/"