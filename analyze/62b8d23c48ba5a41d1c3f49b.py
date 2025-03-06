def popitem(self):
    """
    Eliminar y devolver el par (clave, valor) más recientemente utilizado.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self))
    value = self.pop(key)
    return (key, value)