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
    while path.startswith('/') or path.startswith('\\/'):
        path = path[1:] if path.startswith('/') else path[2:]
    while path.endswith('/') or path.endswith('\\/'):
        path = path[:-1] if path.endswith('/') else path[:-2]
    return path