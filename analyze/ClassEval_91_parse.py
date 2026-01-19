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
    fixed_path = self.fix_path(path)
    if not fixed_path:
        return
    path_segments = fixed_path.split('/')
    for segment in path_segments:
        if segment:
            try:
                decoded_segment = urllib.parse.unquote(segment, encoding=charset)
                self.segments.append(decoded_segment)
            except (UnicodeDecodeError, LookupError):
                self.segments.append(segment)
    self.with_end_tag = path.endswith('/')