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
            if key < 0 or key >= len(self):
                raise IndexError("Indice fuori dai limiti")
            result[self.get_key(key)] = self.get_value(key)
        else:
            result[key] = self.get_value_by_key(key) if self.has_key(key) else None
    if not keys:
        for i in range(len(self)):
            result[self.get_key(i)] = self.get_value(i)
    return result