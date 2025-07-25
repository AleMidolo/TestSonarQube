def popitem(self):
    """
    Eliminar y devolver el par `(clave, valor)` que fue insertado primero.
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get first key-value pair from ordered dict
    key = next(iter(self))
    value = self[key]
    
    # Remove the item
    del self[key]
    
    return (key, value)