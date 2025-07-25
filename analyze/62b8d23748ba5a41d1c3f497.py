def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the minimum frequency
    min_key = min(self.data, key=lambda k: self.data[k][1])
    
    # Remove the item from the dictionary
    value = self.data.pop(min_key)
    
    return (min_key, value[0])  # Return the key and its associated value