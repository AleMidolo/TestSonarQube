def is_valid_ipv4(ip_address):
    """
    Controlla se l'indirizzo IP fornito è un indirizzo IPv4 valido.
    :param ip_address: stringa, l'indirizzo IP da controllare
    :return: bool, True se l'indirizzo IP è valido, False altrimenti
    >>> IpUtil.is_valid_ipv4('192.168.0.123')
    True
    >>> IpUtil.is_valid_ipv4('256.0.0.0')
    False

    """
    if not isinstance(ip_address, str):
        return False
    
    parts = ip_address.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part:
            return False
        
        # Check if part contains only digits
        if not part.isdigit():
            return False
        
        # Check for leading zeros (except for '0' itself)
        if len(part) > 1 and part[0] == '0':
            return False
        
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True