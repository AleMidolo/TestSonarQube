import random

def popitem(self):
    """
    Encontrar, eliminar y devolver un par (clave, valor) aleatorio mediante __choice en la clase.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = random.choice(list(self.keys()))
    value = self.pop(key)
    return (key, value)