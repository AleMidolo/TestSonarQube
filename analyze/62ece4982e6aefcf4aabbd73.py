import re
import sys

def split(s, platform='this'):
    if platform == 'this':
        platform = 1 if sys.platform.startswith(('linux', 'darwin')) else 0

    if platform == 1:  # POSIX
        pattern = r'(?<!\\)(?:\"([^\"]*)\"|\'([^\']*)\'|(\S+))'
    else:  # Windows/CMD
        pattern = r'(?<!\\)(?:\"([^\"]*)\"|(\S+))'

    matches = re.findall(pattern, s)
    result = [m[0] or m[1] or m[2] for m in matches]
    return [arg.replace('\\"', '"').replace("\\'", "'") for arg in result]