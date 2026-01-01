def get_query_params(self):
    """
        Ottieni i parametri della richiesta per l'URL
        :return: dict, Se ha successo, restituisce i parametri della richiesta dell'URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_start = self.url.find('?')
    query_end = self.url.find('#', query_start) if query_start != -1 else -1
    query_string = self.url[query_start + 1:query_end] if query_start != -1 else ''
    params = {}
    for param in query_string.split('&'):
        if '=' in param:
            key, value = param.split('=', 1)
            params[key] = value
    return params