def get_query_params(self):
    """
        URL के लिए अनुरोध पैरामीटर प्राप्त करें
        :return: dict, यदि सफल हो, तो URL के अनुरोध पैरामीटर लौटाएं
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
                pairs = query_string.split('&')
                for pair in pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        query_params[key] = value
                    else:
                        query_params[pair] = None
    return query_params