def get_query_params(self):
    """
    URL के लिए अनुरोध पैरामीटर प्राप्त करें
    :return: dict, यदि सफल हो, तो URL के अनुरोध पैरामीटर लौटाएं
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