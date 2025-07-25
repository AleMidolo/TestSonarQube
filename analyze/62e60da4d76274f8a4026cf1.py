def values(self, *keys):
    """
    以列表的形式返回通过 `self.index` 过滤的键。
    返回记录的值，可以选择性地通过索引或键进行过滤，仅包含特定的值。

    :param keys: 要包含的项目的索引或键；如果未提供任何参数，则包含所有值
    :return: 值的列表
    :rtype: list
    """
    if not keys:
        return list(self.index.values())
    
    return [self.index[key] for key in keys if key in self.index]