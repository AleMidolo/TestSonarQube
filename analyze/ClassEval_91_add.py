def add(self, segment):
    """
        将一个段添加到 UrlPath 的段列表中。
        :param segment: str，要添加的段。
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """
    self.segments.append(segment)