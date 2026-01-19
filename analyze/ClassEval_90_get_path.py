def get_path(self):
    """
    Obtiene la tercera parte de la URL, que es la dirección del recurso
    :return: cadena, Si tiene éxito, devuelve la dirección del recurso de la URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_path()
    "/s?wd=aaa&rsv_spt=1#page"
    """
    from urllib.parse import urlparse
    
    parsed = urlparse(self.url)
    path = parsed.path
    
    # Add query string if present
    if parsed.query:
        path += '?' + parsed.query
    
    # Add fragment if present
    if parsed.fragment:
        path += '#' + parsed.fragment
    
    return path if path else "/"