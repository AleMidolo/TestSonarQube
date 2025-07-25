def popitem(self):
    """
    在类中通过 `__choice` 方法查找、移除并返回一个随机的键值对。
    移除并返回一个随机的键值对。
    """
    if not self:  # 如果字典为空
        raise KeyError('dictionary is empty')
        
    key = self.__choice(list(self.keys()))  # 随机选择一个键
    value = self[key]  # 获取对应的值
    del self[key]  # 删除该键值对
    return key, value  # 返回键值对元组