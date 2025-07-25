def values(self, *keys):
    """
    以列表的形式返回通过 `self.index` 过滤的键。
    返回记录的值，可以选择性地通过索引或键进行过滤，仅包含特定的值。

    :param keys: 要包含的项目的索引或键；如果未提供任何参数，则包含所有值
    :return: 值的列表
    :rtype: list
    """
    if not keys:
        # 如果没有提供键，返回所有值
        return list(self.index.values())
    
    result = []
    for key in keys:
        # 如果key是整数，按索引获取值
        if isinstance(key, int):
            try:
                result.append(list(self.index.values())[key])
            except IndexError:
                continue
        # 否则按键获取值
        else:
            if key in self.index:
                result.append(self.index[key])
    
    return result