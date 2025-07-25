def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # Encuentra la clave con el menor valor de frecuencia
    min_key = min(self.keys(), key=lambda k: self[k])
    
    # Elimina y devuelve el par (clave, valor)
    value = self.pop(min_key)
    return (min_key, value)