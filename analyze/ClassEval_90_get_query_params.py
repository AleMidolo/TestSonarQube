def get_query_params(self):
    """
        获取URL的请求参数
        :return: dict, 如果成功，返回URL的请求参数
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_start = self.url.find('?')
    query_params = {}
    if query_start != -1:
        query_string = self.url[query_start + 1:]
        for param in query_string.split('&'):
            key_value = param.split('=')
            if len(key_value) == 2:
                query_params[key_value[0]] = key_value[1]
    return query_params