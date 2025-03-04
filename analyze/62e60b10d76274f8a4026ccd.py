def data(self, *keys):
    """
    Restituisce le chiavi e i valori di questo record come un dizionario, includendo opzionalmente solo determinati valori in base all'indice o alla chiave. Le chiavi fornite negli elementi che non sono presenti nel record verranno inserite con un valore di :const:`None`; gli indici forniti che sono fuori dai limiti genereranno un'eccezione :exc:`IndexError`.

    :param keys: indici o chiavi degli elementi da includere; se non ne vengono forniti, verranno inclusi tutti i valori  
    :return: dizionario dei valori, indicizzati per nome del campo  
    :raises: :exc:`IndexError` se viene specificato un indice fuori dai limiti  
    """
    result = {}
    if not keys:
        # Include all keys and values
        for key in self.record:
            result[key] = self.record[key]
    else:
        for key in keys:
            if isinstance(key, int):
                if key < 0 or key >= len(self.record):
                    raise IndexError("Index out of bounds")
                result[self.keys[key]] = self.record[self.keys[key]]
            else:
                result[key] = self.record.get(key, None)
    return result