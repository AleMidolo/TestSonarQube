def get_fragment(self):
    """
        Obtiene el fragmento después de '#' en la URL
        :return: cadena, Si tiene éxito, devuelve el fragmento después de '#' de la URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
    fragment_start = self.url.find('#')
    if fragment_start != -1:
        return self.url[fragment_start + 1:]
    return None