def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the minimum usage
    min_key = min(self.usage, key=self.usage.get)
    
    # Remove the key from usage and data
    value = self.data.pop(min_key)
    del self.usage[min_key]
    
    return (min_key, value)