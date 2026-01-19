def get_binary(self):
    """
    Se l'indirizzo IP è valido, restituisce la forma binaria dell'indirizzo IP; altrimenti, restituisce ''
    :return: stringa
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming self has an attribute that stores the IP address (e.g., self.ip)
    # and a method to validate it (e.g., self.is_valid() or similar)
    
    # Check if IP address exists and is valid
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    try:
        # Split the IP address into octets
        octets = self.ip.split('.')
        
        # Validate that we have exactly 4 octets
        if len(octets) != 4:
            return ''
        
        # Convert each octet to binary and validate
        binary_octets = []
        for octet in octets:
            # Check if octet is a valid number
            num = int(octet)
            
            # Check if number is in valid range (0-255)
            if num < 0 or num > 255:
                return ''
            
            # Convert to 8-bit binary (without '0b' prefix)
            binary_octets.append(format(num, '08b'))
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''