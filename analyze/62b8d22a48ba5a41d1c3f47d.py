def pop(self, key, default=__marker):
    """
    D.pop(k[,d]) -> v, rimuove la chiave specificata e restituisce il valore corrispondente.  
    Se la chiave non viene trovata, viene restituito `d` se fornito, altrimenti viene sollevata un'eccezione KeyError.
    """
    try:
        value = self[key]
        del self[key]
        return value
    except KeyError:
        if default is __marker:
            raise KeyError(key)
        return default