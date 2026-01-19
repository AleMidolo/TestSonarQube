def parse(self, path, charset):
    """
    दिए गए पथ स्ट्रिंग को पार्स करता है और UrlPath में खंडों की सूची को भरता है।
    :param path: str, पार्स करने के लिए पथ स्ट्रिंग।
    :param charset: str, पथ स्ट्रिंग का वर्णनात्मक एन्कोडिंग।
    >>> url_path = UrlPath()
    >>> url_path.parse('/foo/bar/', 'utf-8')

    url_path.segments = ['foo', 'bar']
    """
    if not path:
        self.segments = []
        return
    
    # Remove leading and trailing slashes
    path = path.strip('/')
    
    # Split by '/' and filter out empty strings
    if path:
        self.segments = [segment for segment in path.split('/') if segment]
    else:
        self.segments = []