def is_valid(self):
    """
        जज करें कि IP पता मान्य है या नहीं, अर्थात्, क्या IP पता चार दशमलव अंकों से बना है जो '.' द्वारा अलग किए गए हैं। प्रत्येक अंक 0 के बराबर या उससे बड़ा और 255 के बराबर या उससे छोटा होना चाहिए।
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    parts = self.ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
    return True