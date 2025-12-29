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
    raw_segments = decoded_path.split('/')
    for segment in raw_segments:
        if segment:
            fixed_segment = self.fix_path(segment)
            if fixed_segment:
                self.segments.append(fixed_segment)
    self.with_end_tag = path.endswith('/')