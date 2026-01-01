def get_scheme(self):
    """
        ottieni lo schema dell'URL
        :return: stringa, Se ha successo, restituisce lo schema dell'URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
    scheme_end = self.url.find('://')
    if scheme_end != -1:
        return self.url[:scheme_end]
    return None