def get_query_params(self):
    """
        Ottieni i parametri della richiesta per l'URL
        :return: dict, Se ha successo, restituisce i parametri della richiesta dell'URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
    query_start = self.url.find('?')
    if query_start == -1:
        return {}
    fragment_start = self.url.find('#')
    if fragment_start != -1:
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