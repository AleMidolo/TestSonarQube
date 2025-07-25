def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self.data))
    value = self.data.pop(key)
    return key, value