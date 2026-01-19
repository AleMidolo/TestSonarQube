def get_query_params(self):
    """
        Obtener los parámetros de la solicitud para la URL
        :return: dict, Si es exitoso, devuelve los parámetros de la solicitud de la URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    path = self.get_path()
    if path is None:
        return {}
    query_start = path.find('?')
    if query_start == -1:
        return {}
    query_string = path[query_start + 1:]
    fragment_start = query_string.find('#')
    if fragment_start != -1:
        query_string = query_string[:fragment_start]
    if not query_string:
        return {}
    params = {}
    pairs = query_string.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
        else:
            params[pair] = ''
    return params