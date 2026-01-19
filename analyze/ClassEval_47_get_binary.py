def get_binary(self):
    """
    Se l'indirizzo IP è valido, restituisce la forma binaria dell'indirizzo IP; altrimenti, restituisce ''
    :return: stringa
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming there's a method to check if IP is valid or the IP is stored in self
    # Common pattern would be self.ip or self.address
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    try:
        # Split the IP address by dots
        octets = self.ip.split('.')
        
        # Validate that we have exactly 4 octets
        if len(octets) != 4:
            return ''
        
        # Convert each octet to binary and validate range
        binary_octets = []
        for octet in octets:
            # Convert to integer and check if it's in valid range (0-255)
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary_octets.append(format(num, '08b'))
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''