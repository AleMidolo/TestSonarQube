def pop(self, key, default=__marker):
    """
    D.pop(k[,d]) -> v, rimuove la chiave specificata e restituisce il valore corrispondente.  
    Se la chiave non viene trovata, viene restituito `d` se fornito, altrimenti viene sollevata un'eccezione KeyError.
    """
    if key in self:
        value = self[key]
        del self[key]
        return value
    elif default is not self.__marker:
        return default
    else:
        raise KeyError(key)