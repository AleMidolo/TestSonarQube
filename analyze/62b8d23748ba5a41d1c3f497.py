def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.data:
        raise KeyError("No items in the dictionary.")
    
    # Find the least frequently used item
    least_used_key = min(self.data, key=lambda k: self.frequency[k])
    
    # Remove the item from the data and frequency tracking
    value = self.data.pop(least_used_key)
    self.frequency.pop(least_used_key)
    
    return least_used_key, value