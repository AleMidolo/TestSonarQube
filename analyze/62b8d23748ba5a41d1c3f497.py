def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Find the least frequently used item
    least_used_key = min(self.usage_count, key=self.usage_count.get)
    
    # Remove the item from the data and usage count
    value = self.data.pop(least_used_key)
    del self.usage_count[least_used_key]
    
    return least_used_key, value