def get_query_params(self):
    """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    path = self.get_path()
    if not path:
        return {}
    query_start = path.find('?')
    if query_start == -1:
        return {}
    query_string = path[query_start + 1:]
    fragment_start = query_string.find('#')
    if fragment_start != -1:
        query_string = query_string[:fragment_start]
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