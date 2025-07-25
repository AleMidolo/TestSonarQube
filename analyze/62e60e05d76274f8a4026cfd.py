def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    if key in self:
        return list(self).index(key)
    else:
        raise ValueError(f"{key} no está en la lista.")