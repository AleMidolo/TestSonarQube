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