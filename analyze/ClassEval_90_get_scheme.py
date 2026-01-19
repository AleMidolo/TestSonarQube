def get_scheme(self):
    """
    ottieni lo schema dell'URL
    :return: stringa, Se ha successo, restituisce lo schema dell'URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_scheme()
    "https"
    """
    from urllib.parse import urlparse
    parsed_url = urlparse(self.url)
    return parsed_url.scheme