def popitem(self):
    """
    Encontrar, eliminar y devolver un par (clave, valor) aleatorio mediante __choice en la clase
    """
    if not self:
        raise KeyError("Dictionary is empty")
        
    from random import choice
    key = choice(list(self.keys()))
    value = self[key]
    del self[key]
    
    return (key, value)