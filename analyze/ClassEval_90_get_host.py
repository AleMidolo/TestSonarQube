def get_host(self):
    """
        Obtiene la segunda parte de la URL, que es el nombre de dominio del host
        :return: cadena, Si tiene éxito, devuelve el nombre de dominio del host de la URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
    scheme_end = self.url.find('://')
    if scheme_end != -1:
        url_without_scheme = self.url[scheme_end + 3:]
        host_end = url_without_scheme.find('/')
        if host_end != -1:
            return url_without_scheme[:host_end]
        return url_without_scheme
    return None