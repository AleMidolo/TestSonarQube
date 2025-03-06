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
    elif platform not in (0, 1):
        raise ValueError("Invalid platform value. Use 0 for Windows/CMD, 1 for POSIX, or 'this' for auto-detection.")

    if platform == 1:
        # POSIX mode
        regex = re.compile(r"""
            (?:[^\s"']+|"[^"]*"|'[^']*')+
        """, re.VERBOSE)
    else:
        # Windows/CMD mode
        regex = re.compile(r"""
            (?:[^\s"]+|"[^"]*")+
        """, re.VERBOSE)

    matches = regex.findall(s)
    return [match.strip('"\'') for match in matches]