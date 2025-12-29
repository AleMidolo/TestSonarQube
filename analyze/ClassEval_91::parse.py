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
        return
    decoded_path = urllib.parse.unquote(path, encoding=charset)
    cleaned_path = decoded_path.strip('/')
    if not cleaned_path:
        return
    path_segments = cleaned_path.split('/')
    for segment in path_segments:
        if segment:
            self.segments.append(segment)
    if path.endswith('/'):
        self.with_end_tag = True