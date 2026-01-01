@staticmethod
def fix_path(path):
    """
        Corregge la stringa del percorso fornita rimuovendo le barre iniziali e finali.
        :param path: str, la stringa del percorso da correggere.
        :return: str, la stringa del percorso corretta.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
    if not path:
        return ''
    while path.startswith('/') or path.startswith('\\/'):
        if path.startswith('\\/'):
            path = path[2:]
        else:
            path = path[1:]
    while path.endswith('/') or path.endswith('\\/'):
        if path.endswith('\\/'):
            path = path[:-2]
        else:
            path = path[:-1]
    return path