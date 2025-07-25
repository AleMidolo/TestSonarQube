def is_ipv4(target):
    """
    Test if IPv4 address or not
    """
    # Check if target is a string
    if not isinstance(target, str):
        return False
        
    # Split into octets
    octets = target.split('.')
    
    # IPv4 must have exactly 4 octets
    if len(octets) != 4:
        return False
        
    # Check each octet
    for octet in octets:
        # Check if octet is numeric
        if not octet.isdigit():
            return False
            
        # Convert to int
        num = int(octet)
        
        # Check range 0-255
        if num < 0 or num > 255:
            return False
            
        # Check for leading zeros
        if len(octet) > 1 and octet[0] == '0':
            return False
            
    return True