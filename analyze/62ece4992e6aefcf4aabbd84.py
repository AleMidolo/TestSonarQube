import re

def is_ipv4(target):
    """
    IPv4 पते की जांच करें या नहीं।
    """
    pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    return bool(re.match(pattern, target))