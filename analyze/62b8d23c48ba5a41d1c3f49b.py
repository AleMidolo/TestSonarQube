def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(कुंजी, मान)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(reversed(self))
    value = self.pop(key)
    return (key, value)