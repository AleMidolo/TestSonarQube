def popitem(self):
    """
    Eliminar y devolver el par `(clave, valor)` que fue insertado primero.
    """
    if not self:
        raise KeyError("El diccionario está vacío")
    key = next(iter(self))
    value = self[key]
    del self[key]
    return key, value