def parse(self, path, charset):
    """
    Analiza una ruta dada y llena la lista de segmentos en UrlPath.
    :param path: str, la cadena de ruta a analizar.
    :param charset: str, la codificación de caracteres de la cadena de ruta.
    >>> url_path = UrlPath()
    >>> url_path.parse('/foo/bar/', 'utf-8')

    url_path.segments = ['foo', 'bar']
    """
    if not path:
        return
    decoded_path = path.encode('utf-8').decode(charset)
    segments = decoded_path.strip('/').split('/')
    self.segments = [self.fix_path(segment) for segment in segments if segment]