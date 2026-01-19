def get_octets(self):
    """
    如果IP地址有效，则返回由"."分隔的四个十进制数字组成的列表；否则，返回一个空列表
    :return: list
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    # Check if the IP address attribute exists
    if not hasattr(self, 'ip_address') or not self.ip_address:
        return []
    
    # Split the IP address by "."
    parts = self.ip_address.split(".")
    
    # Validate that there are exactly 4 parts
    if len(parts) != 4:
        return []
    
    # Validate each octet
    for part in parts:
        # Check if the part is not empty and contains only digits
        if not part or not part.isdigit():
            return []
        
        # Check if there are leading zeros (except for "0" itself)
        if len(part) > 1 and part[0] == '0':
            return []
        
        # Check if the value is in valid range (0-255)
        if int(part) > 255:
            return []
    
    return parts