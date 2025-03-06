def popitem(self):
    """
    Rimuovi e restituisci una coppia `(chiave, valore)` casuale.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)