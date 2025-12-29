def get_fragment(self):
    """
        Ottieni il frammento dopo '#' nell'URL
        :return: stringa, Se ha successo, restituisce il frammento dopo '#' dell'URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
    fragment_start = self.url.find('#')
    if fragment_start != -1:
        return self.url[fragment_start + 1:]
    return None