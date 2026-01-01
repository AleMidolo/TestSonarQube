def parse(self, path, charset):
    """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
    if not path:
        return
    fixed_path = self.fix_path(path)
    if not fixed_path:
        return
    raw_segments = fixed_path.split('/')
    for segment in raw_segments:
        if segment:
            decoded_segment = urllib.parse.unquote(segment, encoding=charset)
            self.segments.append(decoded_segment)