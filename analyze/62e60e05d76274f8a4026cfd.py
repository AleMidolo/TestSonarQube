def index(self, key):
    """
    Restituisce l'indice dell'elemento specificato.

    :param key: una chiave  
    :return: indice  
    :rtype: int
    """
    for i, item in enumerate(self):
        if item == key:
            return i
    raise ValueError(f"{key} non è presente nella lista.")