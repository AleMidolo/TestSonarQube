import urllib.parse


class UrlPath:
    def __init__(self):
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        self.segments.append(self.fix_path(segment))

    def parse(self, path, charset):
        if path:
            self.with_end_tag = path.endswith('/')
            path = self.fix_path(path)
            if path:
                self._parse_segments(path, charset)

    def _parse_segments(self, path, charset):
        split = path.split('/')
        for seg in split:
            decoded_seg = self._decode_segment(seg, charset)
            self.segments.append(decoded_seg)

    def _decode_segment(self, seg, charset):
        return urllib.parse.unquote(seg, encoding=charset)

    @staticmethod
    def fix_path(path):
        if not path:
            return ''
        return path.strip('/')