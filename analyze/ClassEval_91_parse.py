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
        self.segments = []
        return
    
    # Remove leading and trailing slashes
    path = path.strip('/')
    
    # Split by '/' and filter out empty segments
    if path:
        self.segments = [segment for segment in path.split('/') if segment]
    else:
        self.segments = []