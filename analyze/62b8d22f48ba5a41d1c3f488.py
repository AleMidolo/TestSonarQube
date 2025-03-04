def popitem(self):
    """
    删除与第一个插入的键对应的值，并以元组 `(key, value)` 的格式返回。
    删除并返回第一个插入的 `(key, value)` 键值对。
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # Get first key and value
    key = next(iter(self))
    value = self[key]
    
    # Delete the key-value pair
    del self[key]
    
    # Return as tuple
    return (key, value)