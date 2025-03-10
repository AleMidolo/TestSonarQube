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
        regex = re.compile(r"""
            (?:[^\s"']+|"[^"]*"|'[^']*')+
        """, re.VERBOSE)
    elif platform == 0:  # Windows/CMD
        regex = re.compile(r"""
            (?:[^\s"]+|"[^"]*")+
        """, re.VERBOSE)
    else:
        raise ValueError("Invalid platform value. Use 'this', 1 (POSIX), or 0 (Windows/CMD).")
    
    return [match.group(0) for match in regex.finditer(s)]