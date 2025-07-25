def popitem(self):
    """
    सबसे हाल ही में उपयोग किए गए `(कुंजी, मान)` जोड़े को हटाएं और वापस करें।
    """
    if not self:
        raise KeyError("Dictionary is empty")
    key = next(reversed(self))
    value = self[key]
    del self[key]
    return key, value