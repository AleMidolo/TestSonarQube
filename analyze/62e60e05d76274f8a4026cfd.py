def index(self, key):
    """
    Restituisce l'indice dell'elemento specificato.

    :param key: una chiave  
    :return: indice  
    :rtype: int
    """
    for idx, element in enumerate(self):
        if element == key:
            return idx
    raise ValueError(f"Key {key} not found in the collection.")