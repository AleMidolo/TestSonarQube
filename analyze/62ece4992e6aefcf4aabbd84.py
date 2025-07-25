import re

def is_ipv4(target):
    """
    Verifica se è un indirizzo IPv4 o no.
    """
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return bool(ipv4_pattern.match(target))