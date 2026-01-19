def parse(self, path, charset):
    """
    解析给定的路径字符串并填充 UrlPath 中的段列表。
    :param path: str，要解析的路径字符串。
    :param charset: str，路径字符串的字符编码。
    >>> url_path = UrlPath()
    >>> url_path.parse('/foo/bar/', 'utf-8')

    url_path.segments = ['foo', 'bar']
    """
    if not path:
        self.segments = []
        return
    
    # Remove leading and trailing slashes
    path = path.strip('/')
    
    # If path is empty after stripping, set segments to empty list
    if not path:
        self.segments = []
        return
    
    # Split by '/' and filter out empty strings
    self.segments = [segment for segment in path.split('/') if segment]