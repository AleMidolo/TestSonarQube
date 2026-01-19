def get_host(self):
    """
    Ottieni la seconda parte dell'URL, che è il nome di dominio host
    :return: stringa, Se ha successo, restituisce il nome di dominio host dell'URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_host()
    "www.baidu.com"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    return parsed_url.netloc