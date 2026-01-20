@staticmethod
def is_valid_ipv6(ip_address):
    """
    Verifica si la dirección IP dada es una dirección IPv6 válida.
    :param ip_address:string, la dirección IP a verificar
    :return:bool, True si la dirección IP es válida, False en caso contrario
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
    False

    """
    if not ip_address or not isinstance(ip_address, str):
        return False
    
    # Split by ':' to get segments
    segments = ip_address.split(':')
    
    # IPv6 should have 8 segments (or less if using :: compression)
    # Check for :: (compression) - can only appear once
    if '::' in ip_address:
        # Count occurrences of '::'
        if ip_address.count('::') > 1:
            return False
        
        # Split by '::' to handle compression
        parts = ip_address.split('::')
        if len(parts) > 2:
            return False
        
        # Count total segments
        left_segments = parts[0].split(':') if parts[0] else []
        right_segments = parts[1].split(':') if len(parts) > 1 and parts[1] else []
        
        # Remove empty strings
        left_segments = [s for s in left_segments if s]
        right_segments = [s for s in right_segments if s]
        
        total_segments = len(left_segments) + len(right_segments)
        
        # With compression, we should have less than 8 segments
        if total_segments >= 8:
            return False
        
        # Validate each segment
        all_segments = left_segments + right_segments
    else:
        # No compression, must have exactly 8 segments
        if len(segments) != 8:
            return False
        all_segments = segments
    
    # Validate each segment
    for segment in all_segments:
        # Each segment must be 1-4 hex characters
        if not segment or len(segment) > 4:
            return False
        
        # Check if all characters are valid hexadecimal
        try:
            int(segment, 16)
        except ValueError:
            return False
    
    return True