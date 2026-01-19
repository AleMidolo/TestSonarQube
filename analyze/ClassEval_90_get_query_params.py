def get_query_params(self):
    """
    Get the request parameters for the URL
    :return: dict, If successful, return the request parameters of the URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_query_params()
    {"wd": "aaa", "rsv_spt": "1"}
    """
    from urllib.parse import urlparse, parse_qs
    
    parsed_url = urlparse(self.url)
    query_params = parse_qs(parsed_url.query, keep_blank_values=True)
    
    # parse_qs returns values as lists, so we need to extract single values
    result = {}
    for key, value in query_params.items():
        result[key] = value[0] if len(value) == 1 else value
    
    return result