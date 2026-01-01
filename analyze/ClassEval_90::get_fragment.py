def get_fragment(self):
    """
        URL में '#' के बाद का फ्रैगमेंट प्राप्त करें
        :return: स्ट्रिंग, यदि सफल हो, तो URL के '#' के बाद का फ्रैगमेंट लौटाएं
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
    fragment_start = self.url.find('#')
    if fragment_start != -1:
        return self.url[fragment_start + 1:]
    return None