def data(self, *keys):
    """
    Restituisce le chiavi e i valori di questo record come un dizionario, includendo opzionalmente solo determinati valori in base all'indice o alla chiave. 
    Le chiavi fornite negli elementi che non sono presenti nel record verranno inserite con un valore di :const:`None`; 
    gli indici forniti che sono fuori dai limiti genereranno un'eccezione :exc:`IndexError`.

    :param keys: indici o chiavi degli elementi da includere; se non ne vengono forniti, verranno inclusi tutti i valori  
    :return: dizionario dei valori, indicizzati per nome del campo  
    :raises: :exc:`IndexError` se viene specificato un indice fuori dai limiti  
    """
    # Assuming self._data is a dictionary or list-like structure that holds the record data
    if not keys:
        return dict(self._data) if hasattr(self, '_data') else {}
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self._data):
                raise IndexError("Index out of bounds")
            result[key] = self._data[key]
        else:
            result[key] = self._data.get(key, None) if hasattr(self._data, 'get') else None
    
    return result