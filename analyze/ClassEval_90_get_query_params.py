def get_query_params(self):
    """
        获取URL的请求参数
        :return: dict, 如果成功，返回URL的请求参数
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_params = {}
    path = self.get_path()
    if path:
        query_start = path.find('?')
        if query_start != -1:
            query_string = path[query_start + 1:]
            fragment_start = query_string.find('#')
            if fragment_start != -1:
                query_string = query_string[:fragment_start]
            if query_string:
                params = query_string.split('&')
                for param in params:
                    if '=' in param:
                        key, value = param.split('=', 1)
                        query_params[key] = value
                    else:
                        query_params[param] = None
    return query_params