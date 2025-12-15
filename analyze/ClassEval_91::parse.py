import urllib.parse

class UrlPath: 
    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')
    
        url_path.segments = ['foo', 'bar']
        """
        self.segments.append(self.fix_path(segment))
    
    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('\/foo\/bar\/')
        'foo\/bar'
        """
        if not path:
            return ''

        segment_str = path.strip('\/')
        return segment_str

    def parse(self, path, charset):
        """
        Analizza una data stringa di percorso e popola la lista dei segmenti in UrlPath.
        :param path: str, la stringa di percorso da analizzare.
        :param charset: str, la codifica dei caratteri della stringa di percorso.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
        decoded_path = urllib.parse.unquote(path, encoding=charset)
        segments = decoded_path.strip('/').split('/')
        self.segments = [self.fix_path(segment) for segment in segments if segment]