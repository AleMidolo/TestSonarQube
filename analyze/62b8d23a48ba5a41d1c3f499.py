def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(key, value)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError("dictionary is empty")
    key = next(reversed(self))
    value = self[key]
    del self[key]
    return key, value