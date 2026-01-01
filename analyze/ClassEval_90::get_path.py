def get_path(self):
    """
        Get the third part of the URL, which is the resource address
        :return: string, If successful, return the resource address of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
    scheme_end = self.url.find('://')
    path_start = self.url.find('/', scheme_end + 3) if scheme_end != -1 else self.url.find('/')
    if path_start != -1:
        return self.url[path_start:]
    return None