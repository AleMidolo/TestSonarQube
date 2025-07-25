def dict_insert(dic, val, key, *keys):
    """
    向字典中插入嵌套键的值

    要为嵌套键插入值，必须将所有上级键作为方法的参数提供。

    示例：
      dict_insert({}, 'val', 'key1.key2'.split('.'))

    :param dic: 要插入嵌套键值的字典对象
    :param val: 要插入到字典中的值
    :param key: 键链中的第一个键，用于存储值
    :param keys: 键链中的子键
    """
    current = dic
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    current[keys[-1] if keys else key] = val
    return dic