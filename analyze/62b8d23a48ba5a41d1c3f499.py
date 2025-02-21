def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self._order:
        raise KeyError("popitem(): dictionary is empty")
    
    key = self._order.pop(0)
    value = self._data.pop(key)
    return key, value