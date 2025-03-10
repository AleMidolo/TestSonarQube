def index(self, key):
    """
    Restituisce l'indice dell'elemento specificato.

    :param key: una chiave  
    :return: indice  
    :rtype: int
    """
    if key in self:
        return list(self).index(key)
    else:
        raise ValueError(f"{key} non è presente nella struttura dati.")