def popitem(self):
    """
    删除与第一个插入的键对应的值，并以元组 `(key, value)` 的格式返回。
    删除并返回第一个插入的 `(key, value)` 键值对。
    """
    if not self:  # 如果字典为空
        raise KeyError('Dictionary is empty')
        
    # 获取第一个插入的键
    first_key = next(iter(self))
    # 获取对应的值
    value = self[first_key]
    # 删除该键值对
    del self[first_key]
    # 返回键值对元组
    return (first_key, value)