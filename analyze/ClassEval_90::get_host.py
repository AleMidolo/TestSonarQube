def get_host(self):
    """
        URL का दूसरा भाग प्राप्त करें, जो होस्ट डोमेन नाम है
        :return: स्ट्रिंग, यदि सफल हो, तो URL का होस्ट डोमेन नाम लौटाएं
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
        else:
            return url_without_scheme
    return None