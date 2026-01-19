def get_fragment(self):
    """
    Obtiene el fragmento después de '#' en la URL
    :return: cadena, Si tiene éxito, devuelve el fragmento después de '#' de la URL
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_fragment()
    "page"
    """
    if hasattr(self, 'url') and self.url:
        if '#' in self.url:
            return self.url.split('#', 1)[1]
    return ""