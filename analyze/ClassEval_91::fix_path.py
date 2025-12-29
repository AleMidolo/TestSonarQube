@staticmethod
def fix_path(path):
    """
        修复给定的路径字符串，通过去除前导和尾随的斜杠。
        :param path: str，要修复的路径字符串。
        :return: str，修复后的路径字符串。
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
    if not path:
        return ''
    while path.startswith('/') or path.startswith('\\'):
        path = path[1:]
    while path.endswith('/') or path.endswith('\\'):
        path = path[:-1]
    return path