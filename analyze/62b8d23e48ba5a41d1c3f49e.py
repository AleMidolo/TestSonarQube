def popitem(self):
    """
    एक यादृच्छिक `(कुंजी, मान)` जोड़ी को हटाएं और लौटाएं।
    """
    if not self.data:
        raise KeyError("popitem(): dictionary is empty")
    key = next(iter(self.data))
    value = self.data[key]
    del self.data[key]
    return key, value