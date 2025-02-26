import re
import platform as sys_platform

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
        platform = 1 if sys_platform.system() != 'Windows' else 0

    if platform == 1:  # POSIX
        regex = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+))'
    elif platform == 0:  # Windows
        regex = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+)|(\S+))'
    else:
        raise ValueError("Unsupported platform value")

    matches = re.findall(regex, s)
    result = []
    for match in matches:
        result.append(next(filter(None, match)))  # Get the first non-empty group

    return result