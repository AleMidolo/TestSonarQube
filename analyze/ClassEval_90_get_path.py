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
    
    # 构建路径部分：path + query + fragment
    path = parsed.path if parsed.path else "/"
    
    if parsed.query:
        path += "?" + parsed.query
    
    if parsed.fragment:
        path += "#" + parsed.fragment
    
    return path