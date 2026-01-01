def get_fragment(self):
    """
        获取URL中'#'后面的片段
        :return: 字符串，如果成功，返回URL中'#'后的片段
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
    fragment_start = self.url.find('#')
    if fragment_start != -1:
        return self.url[fragment_start + 1:]
    return None