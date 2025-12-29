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
        return
    cleaned_path = path.strip('/')
    if not cleaned_path:
        return
    raw_segments = cleaned_path.split('/')
    for segment in raw_segments:
        if segment:
            try:
                decoded_segment = urllib.parse.unquote(segment, encoding=charset)
                self.segments.append(decoded_segment)
            except (UnicodeDecodeError, LookupError):
                self.segments.append(segment)