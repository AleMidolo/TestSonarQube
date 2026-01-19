def add(self, segment):
    """
        Agrega un segmento a la lista de segmentos en el UrlPath.
        :param segment: str, el segmento a agregar.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """
    if segment:
        self.segments.append(segment)