def parse(self, path, charset):
    """
        Analizza una data stringa di percorso e popola la lista dei segmenti in UrlPath.
        :param path: str, la stringa di percorso da analizzare.
        :param charset: str, la codifica dei caratteri della stringa di percorso.
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