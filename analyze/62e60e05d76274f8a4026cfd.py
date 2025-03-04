def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    for i in range(len(self)):
        if self[i] == key:
            return i
    raise ValueError(f"{key} is not in list")