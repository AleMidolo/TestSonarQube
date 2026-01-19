def parse(self, path, charset):
    """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
    decoded_path = urllib.parse.unquote(path, encoding=charset)
    self.segments = [self.fix_path(segment) for segment in decoded_path.split('/') if segment]