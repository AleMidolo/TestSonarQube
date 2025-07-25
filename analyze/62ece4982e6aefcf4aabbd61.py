def _dictsum(dicts):
    """
    将字典中具有相同键的值相加，并返回一个新的字典。  
    示例：
      给定两个字典：`dict1: {'a': 1, 'b': 2}` 和 `dict2: {'a': 5, 'b': 0}`  
      返回一个字典：`dic: {'a': 6, 'b': 2}`  

    返回值：字典（dict）

    合并由可迭代字典提供的字典的值。

    >>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
    {'a': 6, 'b': 2}
    """
    if not dicts:
        return {}
        
    # 获取所有字典中的所有唯一键
    all_keys = set().union(*dicts)
    
    # 创建结果字典
    result = {}
    
    # 对每个键,计算所有字典中该键对应值的和
    for key in all_keys:
        result[key] = sum(d.get(key, 0) for d in dicts)
        
    return result