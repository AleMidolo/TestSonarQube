def get_path(self):
    """
        Obtiene la tercera parte de la URL, que es la dirección del recurso
        :return: cadena, Si tiene éxito, devuelve la dirección del recurso de la URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
    scheme_end = self.url.find('://')
    if scheme_end != -1:
        url_without_scheme = self.url[scheme_end + 3:]
        host_end = url_without_scheme.find('/')
        if host_end != -1:
            return url_without_scheme[host_end:]
        return '/'
    return None