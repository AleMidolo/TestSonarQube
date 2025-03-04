def index(self, key):
    """
    Return the index of the given item.
    
    :param key: a key
    :return: index 
    :rtype: int
    """
    for i in range(len(self)):
        if self[i] == key:
            return i
    raise ValueError(f"{key} is not in sequence")