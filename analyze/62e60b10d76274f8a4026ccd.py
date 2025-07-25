def data(self, *keys):
    """
    Restituisce le chiavi e i valori di questo record come un dizionario, includendo opzionalmente solo determinati valori in base all'indice o alla chiave. Le chiavi fornite negli elementi che non sono presenti nel record verranno inserite con un valore di :const:`None`; gli indici forniti che sono fuori dai limiti genereranno un'eccezione :exc:`IndexError`.

    :param keys: indici o chiavi degli elementi da includere; se non ne vengono forniti, verranno inclusi tutti i valori  
    :return: dizionario dei valori, indicizzati per nome del campo  
    :raises: :exc:`IndexError` se viene specificato un indice fuori dai limiti  
    """
    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self.record):
                raise IndexError("Index out of bounds")
            result[self.field_names[key]] = self.record[key]
        else:
            result[key] = self.record.get(key, None)
    
    if not keys:
        for i, value in enumerate(self.record):
            result[self.field_names[i]] = value
            
    return result