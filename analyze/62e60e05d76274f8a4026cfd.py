def index(self, key):
    """    
    दिए गए आइटम का इंडेक्स (स्थान) लौटाता है।

    :param key: एक कुंजी 
    :return: इंडेक्स 
    :rtype: int
    """
    for idx, item in enumerate(self.items):
        if item == key:
            return idx
    raise ValueError(f"{key} is not in the list")