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
        platform = 1 if sys.platform in ['linux', 'darwin'] else 0

    if platform == 1:  # POSIX
        pattern = r'''(?x)            # verbose regex
            (?:                     # non-capturing group for the whole pattern
                "([^"\\]*(?:\\.[^"\\]*)*)"  # double-quoted string
                | '([^'\\]*(?:\\.[^'\\]*)*)'  # single-quoted string
                | ([^\s"']+)       # unquoted string
            )
        '''
    elif platform == 0:  # Windows/CMD
        pattern = r'''(?x)            # verbose regex
            (?:                     # non-capturing group for the whole pattern
                "([^"\\]*(?:\\.[^"\\]*)*)"  # double-quoted string
                | ([^"\s]+)        # unquoted string
            )
        '''
    else:
        raise ValueError("Unsupported platform value")

    matches = re.findall(pattern, s)
    return [m[0] or m[1] or m[2] for m in matches]