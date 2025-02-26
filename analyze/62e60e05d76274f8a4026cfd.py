def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    for idx, value in enumerate(self):
        if value == key:
            return idx
    raise ValueError(f"{key} no está en la lista")