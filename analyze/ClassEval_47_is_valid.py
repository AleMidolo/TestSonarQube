def is_valid(self):
    """
    判断IP地址是否有效，即IP地址是否由四个十进制数字组成，并且用'.'分隔。每个数字大于等于0且小于等于255。
    :return: bool
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.is_valid()
    True
    """
    if not hasattr(self, 'ip') and not hasattr(self, 'address'):
        return False
    
    ip_str = self.ip if hasattr(self, 'ip') else self.address
    
    if not isinstance(ip_str, str):
        return False
    
    parts = ip_str.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part:
            return False
        
        if not part.isdigit():
            return False
        
        if part[0] == '0' and len(part) > 1:
            return False
        
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True