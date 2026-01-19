def get_path(self):
    """
    Ottieni la terza parte dell'URL, che è l'indirizzo della risorsa
    :return: stringa, Se ha successo, restituisce l'indirizzo della risorsa dell'URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_path()
    "/s?wd=aaa&rsv_spt=1#page"
    """
    from urllib.parse import urlparse
    
    parsed = urlparse(self.url)
    path = parsed.path
    
    if parsed.query:
        path += '?' + parsed.query
    
    if parsed.fragment:
        path += '#' + parsed.fragment
    
    return path if path else '/'