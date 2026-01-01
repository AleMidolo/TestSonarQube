@staticmethod
def fix_path(path):
    """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
    if not path:
        return ''
    while path.startswith('/') or path.startswith('\\/'):
        if path.startswith('/'):
            path = path[1:]
        else:
            path = path[2:]
    while path.endswith('/') or path.endswith('\\/'):
        if path.endswith('/'):
            path = path[:-1]
        else:
            path = path[:-2]
    return path