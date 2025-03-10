def data(self, *keys):
    """
    Restituisce le chiavi e i valori di questo record come un dizionario, includendo opzionalmente solo determinati valori in base all'indice o alla chiave. 
    Le chiavi fornite negli elementi che non sono presenti nel record verranno inserite con un valore di :const:`None`; 
    gli indici forniti che sono fuori dai limiti genereranno un'eccezione :exc:`IndexError`.

    :param keys: indici o chiavi degli elementi da includere; se non ne vengono forniti, verranno inclusi tutti i valori  
    :return: dizionario dei valori, indicizzati per nome del campo  
    :raises: :exc:`IndexError` se viene specificato un indice fuori dai limiti  
    """
    result = {}
    if not keys:
        # Se non vengono fornite chiavi, restituisci tutti i valori
        for key in self.__dict__:
            result[key] = self.__dict__[key]
    else:
        for key in keys:
            if isinstance(key, int):
                # Se la chiave è un indice, verifica che sia valido
                if key < 0 or key >= len(self.__dict__):
                    raise IndexError("Indice fuori dai limiti")
                # Converti l'indice in una chiave effettiva
                key = list(self.__dict__.keys())[key]
            # Aggiungi la chiave al risultato, anche se non esiste (valore None)
            result[key] = self.__dict__.get(key, None)
    return result