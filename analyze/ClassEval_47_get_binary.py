def get_binary(self):
    """
    Se l'indirizzo IP è valido, restituisce la forma binaria dell'indirizzo IP; altrimenti, restituisce ''
    :return: stringa
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming there's a method to check if IP is valid or an attribute storing the IP
    # Common pattern would be self.ip_address or similar
    if not hasattr(self, 'ip_address') or not self.ip_address:
        return ''
    
    try:
        # Split the IP address into octets
        octets = self.ip_address.split('.')
        
        # Validate IP address format
        if len(octets) != 4:
            return ''
        
        binary_octets = []
        for octet in octets:
            # Convert to integer and validate range
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary_octets.append(format(num, '08b'))
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''