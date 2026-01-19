def is_valid(self):
    """
    जज करें कि IP पता मान्य है या नहीं, अर्थात्, क्या IP पता चार दशमलव अंकों से बना है जो '.' द्वारा अलग किए गए हैं। प्रत्येक अंक 0 के बराबर या उससे बड़ा और 255 के बराबर या उससे छोटा होना चाहिए।
    :return: bool
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.is_valid()
    True
    """
    try:
        # Split the IP address by '.'
        parts = self.ip.split('.')
        
        # Check if there are exactly 4 parts
        if len(parts) != 4:
            return False
        
        # Check each part
        for part in parts:
            # Check if part is empty
            if not part:
                return False
            
            # Check if part contains only digits
            if not part.isdigit():
                return False
            
            # Check for leading zeros (except for '0' itself)
            if len(part) > 1 and part[0] == '0':
                return False
            
            # Convert to integer and check range
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    except:
        return False