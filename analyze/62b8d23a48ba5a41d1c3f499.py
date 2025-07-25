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
    if first_node.next:
        first_node.next.prev = self.head
    else:
        self.tail = self.head
        
    # Eliminar la entrada del diccionario
    del self.cache[key]
    self.size -= 1
    
    return (key, value)