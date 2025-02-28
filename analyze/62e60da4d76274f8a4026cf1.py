def values(self, *keys):
    """
    Restituisce i valori del record, con la possibilità di filtrare per includere solo determinati valori in base all'indice o alla chiave.

    :param keys: indici o chiavi degli elementi da includere; se non viene fornito nessun parametro, verranno inclusi tutti i valori  
    :return: lista di valori  
    :rtype: list
    """
    if not keys:
        return list(self.__dict__.values())
    else:
        return [self.__dict__.get(key) for key in keys]