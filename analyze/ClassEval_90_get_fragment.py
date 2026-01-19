def get_fragment(self):
    """
    URL में '#' के बाद का फ्रैगमेंट प्राप्त करें
    :return: स्ट्रिंग, यदि सफल हो, तो URL के '#' के बाद का फ्रैगमेंट लौटाएं
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_fragment()
    "page"
    """
    if hasattr(self, 'url') and self.url:
        if '#' in self.url:
            return self.url.split('#', 1)[1]
    return None