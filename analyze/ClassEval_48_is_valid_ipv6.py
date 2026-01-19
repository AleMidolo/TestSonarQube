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
    if len(parts) > 8 or len(parts) < 3:
        return False
    
    # Check for :: (compression) - can only appear once
    empty_count = 0
    for i, part in enumerate(parts):
        if part == '':
            empty_count += 1
    
    # If there are empty parts, they should be consecutive (representing ::)
    if empty_count > 0:
        # :: can appear at start, middle, or end
        # Count consecutive empty strings
        if empty_count == 1:
            # Single empty string only valid at start or end
            if parts[0] != '' and parts[-1] != '':
                return False
        elif empty_count > 1:
            # Multiple empty strings should be consecutive
            empty_indices = [i for i, p in enumerate(parts) if p == '']
            for i in range(len(empty_indices) - 1):
                if empty_indices[i+1] - empty_indices[i] != 1:
                    return False
            # With compression, total groups should be less than 8
            non_empty_parts = [p for p in parts if p != '']
            if len(non_empty_parts) >= 8:
                return False
    else:
        # Without compression, must have exactly 8 groups
        if len(parts) != 8:
            return False
    
    # Validate each non-empty part
    for part in parts:
        if part == '':
            continue
        
        # Each part should be 1-4 hex digits
        if len(part) > 4 or len(part) < 1:
            return False
        
        # Check if all characters are valid hex digits
        try:
            int(part, 16)
        except ValueError:
            return False
    
    return True