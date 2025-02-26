import re

def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, target):
        parts = target.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False