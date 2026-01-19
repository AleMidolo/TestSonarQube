def __init__(self, url):
    """
    初始化 URLHandler
    :param url: 完整的 URL 字符串
    """
    self.url = url
    self.parsed_url = urllib.parse.urlparse(url)