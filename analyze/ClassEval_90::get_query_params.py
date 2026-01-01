def get_query_params(self):
    """
        获取URL的请求参数
        :return: dict, 如果成功，返回URL的请求参数
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_start = self.url.find('?')
    fragment_start = self.url.find('#')
    if query_start == -1:
        return {}
    if fragment_start != -1 and fragment_start > query_start:
        query_string = self.url[query_start + 1:fragment_start]
    else:
        query_string = self.url[query_start + 1:]
    params = {}
    if query_string:
        pairs = query_string.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                params[key] = value
            else:
                params[pair] = ''
    return params