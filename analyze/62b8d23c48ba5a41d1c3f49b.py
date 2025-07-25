def popitem(self):
    """
    Eliminar y devolver el par (clave, valor) más recientemente utilizado.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self.data.popitem()
    return key, value