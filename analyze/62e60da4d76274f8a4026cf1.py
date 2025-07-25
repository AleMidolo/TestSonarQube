def values(self, *keys):
    """
    Restituisce i valori del record, con la possibilità di filtrare per includere solo determinati valori in base all'indice o alla chiave.

    :param keys: indici o chiavi degli elementi da includere; se non viene fornito nessun parametro, verranno inclusi tutti i valori
    :return: lista di valori
    :rtype: list
    """
    if not keys:
        # Se non sono specificate chiavi, restituisce tutti i valori
        return list(self._values)
    
    result = []
    for key in keys:
        if isinstance(key, int):
            # Se la chiave è un indice numerico
            if 0 <= key < len(self._values):
                result.append(self._values[key])
        else:
            # Se la chiave è una stringa
            try:
                index = self._fields.index(key)
                result.append(self._values[index])
            except ValueError:
                pass
    
    return result