def get_path(self):
    """
        Ottieni la terza parte dell'URL, che è l'indirizzo della risorsa
        :return: stringa, Se ha successo, restituisce l'indirizzo della risorsa dell'URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
    scheme_end = self.url.find('://')
    path_start = self.url.find('/', scheme_end + 3)
    fragment_start = self.url.find('#')
    if path_start != -1:
        if fragment_start != -1:
            return self.url[path_start:fragment_start]
        return self.url[path_start:]
    return None