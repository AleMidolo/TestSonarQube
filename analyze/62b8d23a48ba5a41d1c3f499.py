def popitem(self):
    """
    Rimuove e restituisce la coppia `(chiave, valore)` meno recentemente utilizzata.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Assuming self.data is an OrderedDict or similar structure
    key, value = self.data.popitem(last=False)  # Remove the first item (least recently used)
    return key, value