def parse(self, path, charset):
    """
    Parses a given path string and populates the list of segments in the UrlPath.
    :param path: str, the path string to parse.
    :param charset: str, the character encoding of the path string.
    >>> url_path = UrlPath()
    >>> url_path.parse('/foo/bar/', 'utf-8')

    url_path.segments = ['foo', 'bar']
    """
    # Initialize segments list if it doesn't exist
    if not hasattr(self, 'segments'):
        self.segments = []
    else:
        self.segments = []
    
    # Handle empty or None path
    if not path:
        return
    
    # Remove leading and trailing slashes
    path = path.strip('/')
    
    # If path is empty after stripping, return empty segments
    if not path:
        return
    
    # Split by '/' and filter out empty strings
    self.segments = [segment for segment in path.split('/') if segment]