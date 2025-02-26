def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    for i, element in enumerate(self):
        if element == key:
            return i
    raise ValueError(f"{key} no está en la lista.")