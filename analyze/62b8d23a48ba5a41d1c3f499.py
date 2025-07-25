def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos recientemente utilizado.
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    # Obtener el primer elemento (menos recientemente usado)
    first_node = self.head.next
    key = first_node.key
    value = first_node.value
    
    # Eliminar el nodo
    self.head.next = first_node.next
    first_node.next.prev = self.head
    
    # Actualizar el tamaño
    self.size -= 1
    
    # Eliminar la entrada del diccionario
    del self.cache[key]
    
    return (key, value)