def index(self, key):
    """    
    दिए गए आइटम का इंडेक्स (स्थान) लौटाता है।

    :param key: एक कुंजी 
    :return: इंडेक्स 
    :rtype: int
    """
    for i in range(len(self)):
        if self[i] == key:
            return i
    raise ValueError(f"{key} is not in list")