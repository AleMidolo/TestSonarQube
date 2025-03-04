def popitem(self):
    """
    移除并返回最久未使用的键值对。
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # 获取最久未使用的键值对(链表头部)
    key = self.head.next.key
    value = self[key]
    
    # 从字典和双向链表中删除该节点
    self._remove(key)
    del self[key]
    
    return key, value