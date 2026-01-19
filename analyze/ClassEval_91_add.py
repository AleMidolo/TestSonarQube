def add(self, segment):
    """
    Aggiunge un segmento alla lista di segmenti in UrlPath.
    :param segment: str, il segmento da aggiungere.
    >>> url_path = UrlPath()
    >>> url_path.add('foo')
    >>> url_path.add('bar')

    url_path.segments = ['foo', 'bar']
    """
    if not hasattr(self, 'segments'):
        self.segments = []
    self.segments.append(segment)