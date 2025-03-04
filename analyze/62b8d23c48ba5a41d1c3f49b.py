def popitem(self):
    """
    Eliminar y devolver el par (clave, valor) más recientemente utilizado.
    """
    if not self.cache:  # Si el cache está vacío
        raise KeyError("Cache is empty")
        
    # Obtener la clave más recientemente utilizada (última en el orden)
    key = next(reversed(self.order))
    
    # Obtener el valor asociado
    value = self.cache[key]
    
    # Eliminar la entrada del cache y del orden
    del self.cache[key]
    self.order.remove(key)
    
    # Devolver el par (clave, valor)
    return (key, value)