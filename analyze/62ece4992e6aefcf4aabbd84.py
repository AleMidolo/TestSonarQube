import re

def is_ipv4(target):
    """
    Verifica se è un indirizzo IPv4 o no.
    """
    # Regular expression pattern for IPv4
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    
    # Check if the target matches the IPv4 pattern
    if re.match(ipv4_pattern, target):
        return True
    else:
        return False