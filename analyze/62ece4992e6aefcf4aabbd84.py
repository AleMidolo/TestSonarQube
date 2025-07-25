import re

def is_ipv4(target):
    """
    IPv4 पते की जांच करें या नहीं।
    """
    # IPv4 address pattern
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return bool(pattern.match(target))