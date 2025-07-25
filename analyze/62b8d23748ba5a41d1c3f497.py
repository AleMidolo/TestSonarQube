def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.cache:  # Si el cache está vacío
        raise KeyError("Cache is empty")
        
    # Encontrar la frecuencia mínima
    min_freq = min(self.freq_list.keys())
    
    # Obtener el LRU de los elementos con frecuencia mínima
    lru_key = self.freq_list[min_freq].pop()
    
    # Si la lista de frecuencia queda vacía, eliminarla
    if not self.freq_list[min_freq]:
        del self.freq_list[min_freq]
        
    # Obtener el valor asociado a la clave
    value = self.cache[lru_key]
    
    # Eliminar la entrada del cache
    del self.cache[lru_key]
    del self.key_freq[lru_key]
    
    return (lru_key, value)