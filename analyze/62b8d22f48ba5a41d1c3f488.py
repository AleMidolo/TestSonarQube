def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` inserita per prima.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    first_key = next(iter(self.data))
    value = self.data.pop(first_key)
    return first_key, value