def is_valid(self):
    """
    Giudica se l'indirizzo IP è valido, cioè se l'indirizzo IP è composto da quattro cifre decimali separate da '.'. Ogni cifra è maggiore o uguale a 0 e minore o uguale a 255.
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
        
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True