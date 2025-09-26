import urllib.parse


class UrlPath:
    def __init__(self):
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        self.segments.append(self.fix_path(segment))

    def parse(self, path, charset):
        if path:
            self._set_end_tag(path)
            path = self.fix_path(path)
            if path:
                self._decode_segments(path, charset)

    def _set_end_tag(self, path):
        if path.endswith('/'):
            self.with_end_tag = True

    def _decode_segments(self, path, charset):
        split = path.split('/')
        for seg in split:
            decoded_seg = urllib.parse.unquote(seg, encoding=charset)
            self.segments.append(decoded_seg)

    @staticmethod
    def fix_path(path):
        if not path:
            return ''

        segment_str = path.strip('/')
        return segment_str