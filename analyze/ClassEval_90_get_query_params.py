def get_query_params(self):
    """
    获取URL的请求参数
    :return: dict, 如果成功，返回URL的请求参数
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_query_params()
    {"wd": "aaa", "rsv_spt": "1"}
    """
    from urllib.parse import urlparse, parse_qs
    
    parsed_url = urlparse(self.url)
    query_params = parse_qs(parsed_url.query, keep_blank_values=True)
    
    # parse_qs returns values as lists, convert to single values
    result = {}
    for key, value in query_params.items():
        result[key] = value[0] if len(value) == 1 else value
    
    return result