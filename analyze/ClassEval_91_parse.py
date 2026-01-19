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
    cleaned_path = decoded_path.strip('/')
    if not cleaned_path:
        return
    path_segments = cleaned_path.split('/')
    for segment in path_segments:
        if segment:
            self.segments.append(segment)
    if path.endswith('/'):
        self.with_end_tag = True