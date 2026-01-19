def get_binary(self):
    """
    यदि IP पता मान्य है, तो IP पते का बाइनरी रूप लौटाएं; अन्यथा, '' लौटाएं
    :return: स्ट्रिंग
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Validate IP address
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    try:
        # Split IP address into octets
        octets = self.ip.split('.')
        
        # Check if there are exactly 4 octets
        if len(octets) != 4:
            return ''
        
        binary_octets = []
        for octet in octets:
            # Convert to integer and validate range
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary = bin(num)[2:].zfill(8)
            binary_octets.append(binary)
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''