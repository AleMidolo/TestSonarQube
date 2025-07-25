def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    # 找到最少使用的键
    least_used_key = min(self.keys(), key=lambda k: self[k])
    
    # 移除并返回该键值对
    value = self.pop(least_used_key)
    return (least_used_key, value)