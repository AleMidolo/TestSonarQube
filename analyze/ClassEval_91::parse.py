def parse(self, path, charset):
    """
        解析给定的路径字符串并填充 UrlPath 中的段列表。
        :param path: str，要解析的路径字符串。
        :param charset: str，路径字符串的字符编码。
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
    decoded_path = urllib.parse.unquote(path, encoding=charset)
    self.segments = [self.fix_path(segment) for segment in decoded_path.split('/') if segment]