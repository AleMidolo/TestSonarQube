def index(self, key):
    """
    Devuelve el índice del elemento dado.

    :param key: una clave  
    :return: index  
    :rtype: int
    """
    try:
        return self._data.index(key)
    except ValueError:
        return -1