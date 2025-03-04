def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.cache:  # Si el cache está vacío
        raise KeyError("Cache is empty")
        
    # Encontrar la frecuencia mínima
    min_freq = min(self.freq_list.keys())
    
    # Obtener la lista de elementos con esa frecuencia
    lru_items = self.freq_list[min_freq]
    
    # Obtener el elemento menos usado recientemente (el último de la lista)
    key = lru_items.pop()
    
    # Si la lista queda vacía, eliminar la frecuencia
    if not lru_items:
        del self.freq_list[min_freq]
        
    # Obtener el valor asociado a la clave
    value = self.cache[key]
    
    # Eliminar la clave del cache
    del self.cache[key]
    
    # Eliminar la clave del mapeo de frecuencias
    del self.key_freq[key]
    
    return key, value