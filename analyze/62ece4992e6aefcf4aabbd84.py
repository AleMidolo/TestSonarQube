import re

def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, target):
        octets = target.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False