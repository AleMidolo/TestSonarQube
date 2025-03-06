def index(self, key):
    """
    दिए गए आइटम का इंडेक्स (स्थान) लौटाता है।

    :param key: एक कुंजी 
    :return: इंडेक्स 
    :rtype: int
    """
    if key in self:
        return list(self).index(key)
    else:
        raise ValueError(f"{key} not found in the collection.")