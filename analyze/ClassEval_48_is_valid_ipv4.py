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
    
    # Split by dots
    parts = ip_address.split('.')
    
    # Must have exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Check each part
    for part in parts:
        # Empty part is invalid
        if not part:
            return False
        
        # Leading zeros are invalid (except for '0' itself)
        if len(part) > 1 and part[0] == '0':
            return False
        
        # Must be numeric
        if not part.isdigit():
            return False
        
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True