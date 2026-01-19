def get_host(self):
    """
    Obtiene la segunda parte de la URL, que es el nombre de dominio del host
    :return: cadena, Si tiene éxito, devuelve el nombre de dominio del host de la URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_host()
    "www.baidu.com"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    return parsed_url.netloc