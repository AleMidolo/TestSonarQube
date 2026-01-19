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
    
    # 移除开头和结尾的斜杠
    path = path.strip('/')
    
    # 如果路径为空（原始路径只包含斜杠），设置为空列表
    if not path:
        self.segments = []
        return
    
    # 按斜杠分割路径
    segments = path.split('/')
    
    # 过滤掉空字符串段
    self.segments = [segment for segment in segments if segment]