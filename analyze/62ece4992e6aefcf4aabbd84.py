def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    import re
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return bool(ipv4_pattern.match(target))