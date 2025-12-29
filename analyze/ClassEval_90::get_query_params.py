def get_query_params(self):
    """
        URL के लिए अनुरोध पैरामीटर प्राप्त करें
        :return: dict, यदि सफल हो, तो URL के अनुरोध पैरामीटर लौटाएं
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_start = self.url.find('?')
    if query_start != -1:
        query_string = self.url[query_start + 1:]
        params = {}
        for param in query_string.split('&'):
            key_value = param.split('=')
            if len(key_value) == 2:
                params[key_value[0]] = key_value[1]
        return params
    return {}