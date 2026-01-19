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
    return path.strip('/')