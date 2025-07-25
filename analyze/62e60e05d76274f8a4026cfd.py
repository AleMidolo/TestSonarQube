def index(self, key):
    """    
    दिए गए आइटम का इंडेक्स (स्थान) लौटाता है।

    :param key: एक कुंजी 
    :return: इंडेक्स 
    :rtype: int
    """
    try:
        return self.items.index(key)
    except ValueError:
        return -1