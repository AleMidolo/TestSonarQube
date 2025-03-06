def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    for i, item in enumerate(self):
        if item == key:
            return i
    raise ValueError(f"{key} no está en la lista")