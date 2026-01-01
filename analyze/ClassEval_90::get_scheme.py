def get_scheme(self):
    """
        obtener el esquema de la URL
        :return: cadena, Si tiene éxito, devuelve el esquema de la URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
    scheme_end = self.url.find('://')
    if scheme_end != -1:
        return self.url[:scheme_end]
    return None