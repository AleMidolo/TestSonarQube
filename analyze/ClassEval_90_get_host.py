def get_host(self):
    """
        获取 URL 的第二部分，即主机域名
        :return: 字符串，如果成功，返回 URL 的主机域名
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