def get_binary(self):
    """
    Se l'indirizzo IP è valido, restituisce la forma binaria dell'indirizzo IP; altrimenti, restituisce ''
    :return: stringa
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming self has an IP address stored (likely in self.ip or similar)
    # and a method to validate it (or we need to validate here)
    
    # Check if IP is valid
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    try:
        # Split the IP address into octets
        octets = self.ip.split('.')
        
        # Validate IP format
        if len(octets) != 4:
            return ''
        
        # Convert each octet to binary and validate range
        binary_octets = []
        for octet in octets:
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary_octets.append(format(num, '08b'))
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''