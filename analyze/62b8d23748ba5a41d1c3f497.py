def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos utilizado con mayor frecuencia.
    """
    if not self.cache:  # Si el cache está vacío
        raise KeyError("Cache is empty")
        
    # Encontrar la frecuencia mínima
    min_freq = min(self.freq_list.keys())
    
    # Obtener la lista de claves con esa frecuencia
    lru_list = self.freq_list[min_freq]
    
    # Obtener la clave menos usada recientemente (la última de la lista)
    lru_key = lru_list[-1]
    
    # Obtener el valor asociado
    lru_value = self.cache[lru_key].value
    
    # Eliminar la clave del cache y de la lista de frecuencias
    del self.cache[lru_key]
    lru_list.remove(lru_key)
    
    # Si la lista de frecuencia queda vacía, eliminarla
    if not lru_list:
        del self.freq_list[min_freq]
        
    return (lru_key, lru_value)