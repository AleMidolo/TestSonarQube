def get_fragment(self):
    """
    Ottieni il frammento dopo '#' nell'URL
    :return: stringa, Se ha successo, restituisce il frammento dopo '#' dell'URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_fragment()
    "page"
    """
    if hasattr(self, 'url') and self.url:
        if '#' in self.url:
            return self.url.split('#', 1)[1]
    return ""