def popitem(self):
    """
    移除并返回最少使用的键值对。
    """
    if not self:
        raise KeyError('Dictionary is empty')
        
    # 获取最少使用的节点
    node = self.head.next
    
    # 从双向链表中删除该节点
    node.prev.next = node.next 
    node.next.prev = node.prev
    
    # 从哈希表中删除该键值对
    key = node.key
    del self.cache[key]
    
    # 返回键值对
    return (key, node.value)