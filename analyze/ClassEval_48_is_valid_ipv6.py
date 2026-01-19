@staticmethod
def is_valid_ipv6(ip_address):
    """
    检查给定的 IP 地址是否是有效的 IPv6 地址。
    :param ip_address:字符串, 要检查的 IP 地址
    :return:布尔值, 如果 IP 地址有效则返回 True，否则返回 False
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
    False

    """
    if not ip_address or not isinstance(ip_address, str):
        return False
    
    # Split by ':'
    parts = ip_address.split(':')
    
    # IPv6 should have 8 groups (or less if using :: compression)
    # Check for :: (compression)
    if '::' in ip_address:
        # :: can only appear once
        if ip_address.count('::') > 1:
            return False
        
        # Split by :: to handle compression
        left, right = ip_address.split('::', 1)
        left_parts = left.split(':') if left else []
        right_parts = right.split(':') if right else []
        
        # Remove empty strings
        left_parts = [p for p in left_parts if p]
        right_parts = [p for p in right_parts if p]
        
        # Total parts should be less than 8 (since :: represents at least one group)
        if len(left_parts) + len(right_parts) >= 8:
            return False
        
        # Validate each part
        for part in left_parts + right_parts:
            if not part or len(part) > 4:
                return False
            try:
                int(part, 16)
            except ValueError:
                return False
    else:
        # No compression, must have exactly 8 groups
        if len(parts) != 8:
            return False
        
        # Validate each part
        for part in parts:
            if not part or len(part) > 4:
                return False
            try:
                int(part, 16)
            except ValueError:
                return False
    
    return True