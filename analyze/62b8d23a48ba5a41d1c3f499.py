def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos recientemente utilizado.
    """
    if not self.cache:  # Si el cache está vacío
        raise KeyError("Cache is empty")
        
    # Obtener el nodo menos recientemente usado (el último de la lista)
    lru_node = self.tail.prev
    
    # Obtener la clave y valor antes de eliminar
    key = lru_node.key
    value = lru_node.value
    
    # Eliminar el nodo de la lista doblemente enlazada
    self._remove_node(lru_node)
    
    # Eliminar la entrada del diccionario
    del self.cache[key]
    
    return key, value