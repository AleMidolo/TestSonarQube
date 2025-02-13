import re
import os
import platform as sys_platform

def split(s, platform='this'):
    if platform == 'this':
        platform = 1 if sys_platform.system() != 'Windows' else 0
    if platform == 1:  # POSIX
        return re.findall(r'(?:"([^"]*)"|\'([^\']*)|(\S+))', s)
    elif platform == 0:  # Windows/CMD
        return re.findall(r'(?:"([^"]*)"|(\S+))', s)
    else:
        raise ValueError("Unsupported platform value")