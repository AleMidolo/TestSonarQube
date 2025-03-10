def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` utilizzata più di recente.
    """
    if not self:
        raise KeyError("dictionary is empty")
    key = next(reversed(self))
    value = self[key]
    del self[key]
    return key, value