@staticmethod
def fix_path(path):
    """
        दिए गए पथ स्ट्रिंग को ठीक करता है, अग्रणी और अनुक्रमणिका स्लैश को हटाकर।
        :param path: str, ठीक करने के लिए पथ स्ट्रिंग।
        :return: str, ठीक की गई पथ स्ट्रिंग।
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
    if not path:
        return path
    path = path.strip('\\/')
    path = path.strip('/')
    return path