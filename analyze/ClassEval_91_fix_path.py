@staticmethod
def fix_path(path):
    """
        Corrige la ruta dada eliminando las barras inclinadas al principio y al final.
        :param path: str, la cadena de ruta a corregir.
        :return: str, la cadena de ruta corregida.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
    if not path:
        return ''
    while path.startswith('/'):
        path = path[1:]
    while path.endswith('/'):
        path = path[:-1]
    return path