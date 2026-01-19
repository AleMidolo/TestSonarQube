def is_valid_ipv4(ip_address):
    """
    दिए गए IP पते की वैधता की जांच करें कि यह एक वैध IPv4 पता है या नहीं।
    :param ip_address: स्ट्रिंग, जांचने के लिए IP पता
    :return: बूल, यदि IP पता वैध है तो True, अन्यथा False
    >>> IpUtil.is_valid_ipv4('192.168.0.123')
    True
    >>> IpUtil.is_valid_ipv4('256.0.0.0')
    False
    """
    if not isinstance(ip_address, str):
        return False
    
    parts = ip_address.split('.')
    
    # IPv4 address must have exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Each part must not be empty
        if not part:
            return False
        
        # Each part must contain only digits
        if not part.isdigit():
            return False
        
        # No leading zeros allowed (except for '0' itself)
        if len(part) > 1 and part[0] == '0':
            return False
        
        # Each part must be in range 0-255
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True