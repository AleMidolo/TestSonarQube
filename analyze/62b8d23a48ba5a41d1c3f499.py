def popitem(self):
    """
    Elimina y devuelve el par (clave, valor) menos recientemente utilizado.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)