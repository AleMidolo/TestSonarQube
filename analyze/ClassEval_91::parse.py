def parse(self, path, charset):
    """
        Analizza una data stringa di percorso e popola la lista dei segmenti in UrlPath.
        :param path: str, la stringa di percorso da analizzare.
        :param charset: str, la codifica dei caratteri della stringa di percorso.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
    decoded_path = urllib.parse.unquote(path, encoding=charset)
    segments = decoded_path.strip('/').split('/')
    self.segments = [self.fix_path(segment) for segment in segments if segment]