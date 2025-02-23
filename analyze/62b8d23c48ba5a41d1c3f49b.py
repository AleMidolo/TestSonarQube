def popitem(self):  
    """
    Rimuove e restituisce la coppia `(chiave, valore)` utilizzata più di recente.
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    
    # Assuming self.data is an OrderedDict or similar structure
    key, value = self.data.popitem(last=True)
    return key, value