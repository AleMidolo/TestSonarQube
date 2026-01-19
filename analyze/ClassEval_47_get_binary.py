def get_binary(self):
    """
    Si la dirección IP es válida, devuelve la forma binaria de la dirección IP; de lo contrario, devuelve ''
    :return: cadena
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming self has an IP address stored (likely in self.ip or similar)
    # First, validate the IP address
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    try:
        # Split the IP address into octets
        octets = self.ip.split('.')
        
        # Validate that we have exactly 4 octets
        if len(octets) != 4:
            return ''
        
        binary_octets = []
        for octet in octets:
            # Convert to integer and validate range (0-255)
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary = format(num, '08b')
            binary_octets.append(binary)
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''