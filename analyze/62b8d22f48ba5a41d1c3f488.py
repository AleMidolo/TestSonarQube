def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` inserita per prima.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self[key]
    del self[key]
    return key, value