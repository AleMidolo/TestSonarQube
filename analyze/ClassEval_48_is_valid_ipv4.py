def is_valid_ipv4(ip_address):
    """
    检查给定的 IP 地址是否是有效的 IPv4 地址。
    :param ip_address: 字符串，要检查的 IP 地址
    :return: 布尔值，如果 IP 地址有效则返回 True，否则返回 False
    >>> IpUtil.is_valid_ipv4('192.168.0.123')
    True
    >>> IpUtil.is_valid_ipv4('256.0.0.0')
    False

    """
    if not isinstance(ip_address, str):
        return False
    
    parts = ip_address.split('.')
    
    # IPv4 地址必须有 4 个部分
    if len(parts) != 4:
        return False
    
    for part in parts:
        # 检查是否为空字符串
        if not part:
            return False
        
        # 检查是否有前导零（除了单独的 "0"）
        if len(part) > 1 and part[0] == '0':
            return False
        
        # 检查是否全是数字
        if not part.isdigit():
            return False
        
        # 检查数字范围是否在 0-255 之间
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True