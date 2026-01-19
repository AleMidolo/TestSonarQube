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
        self.segments = []
        return
    
    # Remove leading and trailing slashes
    path = path.strip('/')
    
    # Split by '/' and filter out empty strings
    if path:
        self.segments = [segment for segment in path.split('/') if segment]
    else:
        self.segments = []