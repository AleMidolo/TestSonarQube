def add(self, segment):
    """
        UrlPath में सेगमेंट की सूची में एक सेगमेंट जोड़ता है।
        :param segment: str, जोड़ने के लिए सेगमेंट।
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """
    self.segments.append(segment)