def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the key with the least frequency
    least_used_key = min(self.data, key=self.data.get)
    
    # Get the value associated with that key
    value = self.data[least_used_key]
    
    # Remove the key-value pair from the dictionary
    del self.data[least_used_key]
    
    return least_used_key, value