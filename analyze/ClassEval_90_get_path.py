def get_path(self):
    """
    URL का तीसरा भाग प्राप्त करें, जो संसाधन का पता है
    :return: स्ट्रिंग, यदि सफल हो, तो URL के संसाधन का पता लौटाएं
    >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    >>> urlhandler.get_path()
    "/s?wd=aaa&rsv_spt=1#page"
    """
    from urllib.parse import urlparse
    
    parsed_url = urlparse(self.url)
    path = parsed_url.path
    
    # Add query string if present
    if parsed_url.query:
        path += '?' + parsed_url.query
    
    # Add fragment if present
    if parsed_url.fragment:
        path += '#' + parsed_url.fragment
    
    return path if path else "/"