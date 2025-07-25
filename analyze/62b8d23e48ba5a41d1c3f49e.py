def popitem(self):
    """
    एक यादृच्छिक `(कुंजी, मान)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self))
    value = self[key]
    del self[key]
    return key, value