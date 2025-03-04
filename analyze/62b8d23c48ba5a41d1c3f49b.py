def popitem(self):
    """
    移除并返回最近使用的键值对。
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # 获取最近使用的键值对
    key = next(reversed(self))
    value = self[key]
    
    # 从字典中删除该键值对
    del self[key]
    
    return key, value