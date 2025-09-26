import urllib.parse


class UrlPath:
    def __init__(self):
        self._segments = []
        self._with_end_tag = False

    def add(self, segment):
        self._segments.append(self._fix_path(segment))

    def parse(self, path, charset):
        if path:
            self._with_end_tag = path.endswith('/')

            path = self._fix_path(path)
            if path:
                self._parse_segments(path, charset)

    def _parse_segments(self, path, charset):
        split = path.split('/')
        for seg in split:
            decoded_seg = urllib.parse.unquote(seg, encoding=charset)
            self._segments.append(decoded_seg)

    @staticmethod
    def _fix_path(path):
        if not path:
            return ''

        segment_str = path.strip('/')
        return segment_str