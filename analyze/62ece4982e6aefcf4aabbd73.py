import re
import sys

def split(s, platform='this'):
    """
    Multi-platform variant of shlex.split() for command-line splitting.
    For use with subprocess, for argv injection etc. Using fast REGEX.

    platform: 'this' = auto from current platform;
              1 = POSIX;
              0 = Windows/CMD
              (other values reserved)
    """
    if platform == 'this':
        platform = 1 if sys.platform != 'win32' else 0

    if platform == 1:  # POSIX
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+))'
    elif platform == 0:  # Windows
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+)|(\S+)?)'
    else:
        raise ValueError("Unsupported platform value")

    matches = re.findall(pattern, s)
    result = []
    for match in matches:
        result.append(next(filter(None, match)))  # Get the first non-empty group

    return result