def get_path(self):
    """
        URL का तीसरा भाग प्राप्त करें, जो संसाधन का पता है
        :return: स्ट्रिंग, यदि सफल हो, तो URL के संसाधन का पता लौटाएं
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
    scheme_end = self.url.find('://')
    if scheme_end != -1:
        url_without_scheme = self.url[scheme_end + 3:]
        path_start = url_without_scheme.find('/')
        if path_start != -1:
            return url_without_scheme[path_start:]
        return '/'
    return None