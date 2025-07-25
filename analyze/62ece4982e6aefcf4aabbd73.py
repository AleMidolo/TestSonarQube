import re
import platform

def split(s, platform='this'):
    if platform == 'this':
        platform = 1 if os.name == 'posix' else 0

    if platform == 1:  # POSIX style
        return re.findall(r'(?:"([^"]*)"|\'([^\']*)|(\S+))', s)
    elif platform == 0:  # Windows/CMD style
        return re.findall(r'(?:"([^"]*)"|(\S+))', s)
    else:
        raise ValueError("Unsupported platform option.")