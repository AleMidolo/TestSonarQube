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
    cleaned_path = path.strip('/')
    if not cleaned_path:
        return
    raw_segments = cleaned_path.split('/')
    for segment in raw_segments:
        if segment:
            try:
                decoded_segment = urllib.parse.unquote(segment, encoding=charset)
                self.segments.append(self.fix_path(decoded_segment))
            except (UnicodeDecodeError, LookupError):
                self.segments.append(self.fix_path(segment))
    self.with_end_tag = path.endswith('/')