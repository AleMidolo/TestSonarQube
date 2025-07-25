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
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result