def index(self, key):
    """    
    दिए गए आइटम का इंडेक्स (स्थान) लौटाता है।

    :param key: एक कुंजी 
    :return: इंडेक्स 
    :rtype: int
    """
    for i, item in enumerate(self):
        if item == key:
            return i
    raise ValueError(f"{key} is not in the list")