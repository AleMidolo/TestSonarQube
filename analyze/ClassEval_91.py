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
            self.process_path(path, charset)

    def process_path(self, path, charset):
        path = self.fix_path(path)
        if path:
            split = path.split('/')
            for seg in split:
                decoded_seg = self.decode_segment(seg, charset)
                self.segments.append(decoded_seg)

    def decode_segment(self, seg, charset):
        return urllib.parse.unquote(seg, encoding=charset)

    @staticmethod
    def fix_path(path):
        if not path:
            return ''
        return path.strip('/')