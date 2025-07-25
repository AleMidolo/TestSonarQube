import re
import platform

def split(s, platform='this'):
    if platform == 'this':
        platform = 1 if os.name == 'posix' else 0

    if platform == 1:  # POSIX
        pattern = r'(?<!\\)"([^"]*(?:\\.[^"]*)*)"(?!\\)|(?<!\\)\'([^\']*(?:\\.[^\']*)*)\'(?!\\)|(?<!\\)\S+'
    else:  # Windows/CMD
        pattern = r'(?<!\\)"([^"]*(?:\\.[^"]*)*)"(?!\\)|(?<!\\)\S+'

    return re.findall(pattern, s)