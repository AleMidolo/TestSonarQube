def get_fragment(self):
    """
    获取URL中'#'后面的片段
    :return: 字符串，如果成功，返回URL中'#'后的片段
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_fragment()
    "page"
    """
    if hasattr(self, 'url') and self.url:
        if '#' in self.url:
            return self.url.split('#', 1)[1]
        return ""
    return ""