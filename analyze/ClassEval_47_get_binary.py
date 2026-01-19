def get_binary(self):
    """
    如果IP地址有效，返回IP地址的二进制形式；否则，返回''
    :return: 字符串
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # First, validate the IP address
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    parts = self.ip.split('.')
    
    # Check if IP has 4 parts
    if len(parts) != 4:
        return ''
    
    binary_parts = []
    for part in parts:
        try:
            # Convert to integer
            num = int(part)
            # Check if number is in valid range (0-255)
            if num < 0 or num > 255:
                return ''
            # Convert to 8-bit binary (remove '0b' prefix and pad to 8 digits)
            binary_parts.append(format(num, '08b'))
        except ValueError:
            # If conversion to int fails, IP is invalid
            return ''
    
    return '.'.join(binary_parts)