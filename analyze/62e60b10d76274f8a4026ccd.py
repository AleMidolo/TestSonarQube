def data(self, *keys):
    """
    Restituisce le chiavi e i valori di questo record come un dizionario, includendo opzionalmente solo determinati valori in base all'indice o alla chiave. Le chiavi fornite negli elementi che non sono presenti nel record verranno inserite con un valore di :const:`None`; gli indici forniti che sono fuori dai limiti genereranno un'eccezione :exc:`IndexError`.

    :param keys: indici o chiavi degli elementi da includere; se non ne vengono forniti, verranno inclusi tutti i valori  
    :return: dizionario dei valori, indicizzati per nome del campo  
    :raises: :exc:`IndexError` se viene specificato un indice fuori dai limiti  
    """
    if not hasattr(self, '_data'):
        self._data = {}

    result = {}
    if not keys:
        result = self._data.copy()
    else:
        for key in keys:
            if isinstance(key, int):
                if key < 0 or key >= len(self._data):
                    raise IndexError("Indice fuori dai limiti")
                result[list(self._data.keys())[key]] = list(self._data.values())[key]
            else:
                result[key] = self._data.get(key, None)
    return result