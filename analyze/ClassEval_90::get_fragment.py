def get_fragment(self):
    """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
    fragment_start = self.url.find('#')
    if fragment_start != -1:
        return self.url[fragment_start + 1:]
    return None