def index(self, key):
    """
    Restituisce l'indice dell'elemento specificato.

    :param key: una chiave  
    :return: indice  
    :rtype: int
    """
    for idx, value in enumerate(self):
        if value == key:
            return idx
    raise ValueError(f"Key {key} not found in the collection.")