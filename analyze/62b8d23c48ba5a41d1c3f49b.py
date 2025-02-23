def popitem(self):  
    """
    सबसे हाल ही में उपयोग किए गए `(कुंजी, मान)` जोड़े को हटाएं और वापस करें।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self.data.popitem()
    return key, value