def popitem(self):
    """
    Eliminar y devolver el par `(clave, valor)` que fue insertado primero.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get first key and value
    first_key = next(iter(self))
    first_value = self[first_key]
    
    # Remove the item
    del self[first_key]
    
    # Return key-value pair as tuple
    return (first_key, first_value)