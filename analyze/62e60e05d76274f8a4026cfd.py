def index(self, key):
    """
    Restituisce l'indice dell'elemento specificato.

    :param key: una chiave  
    :return: indice  
    :rtype: int
    """
    for i in range(len(self)):
        if self[i] == key:
            return i
    raise ValueError(f"{key} is not in list")