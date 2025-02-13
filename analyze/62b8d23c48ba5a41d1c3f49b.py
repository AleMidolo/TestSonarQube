def popitem(self):
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self._order.popitem()
    del self._data[key]
    return key, value