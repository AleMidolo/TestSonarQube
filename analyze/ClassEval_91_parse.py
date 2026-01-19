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
    decoded_path = urllib.parse.unquote(path, encoding=charset)
    raw_segments = decoded_path.split('/')
    for segment in raw_segments:
        if segment:
            fixed_segment = self.fix_path(segment)
            if fixed_segment:
                self.segments.append(fixed_segment)
    if path.endswith('/'):
        self.with_end_tag = True