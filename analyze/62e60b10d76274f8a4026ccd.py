def data(self, *keys):
    """
    返回由 `RecordExporter` 类的 `transform` 方法处理的键。
    将此记录的键和值以字典形式返回，并可选择按索引或键筛选特定值。对于提供的键，如果记录中不存在，则会以 None 作为默认值插入；如果提供的索引超出范围，则会触发 IndexError。

    :param keys: 要包含的条目的索引或键；如果未提供，将包含所有值
    :return: 一个以字段名称为键的值字典 
    :raises: :exc: 如果指定了超出范围的索引，则会抛出`IndexError`
    """
    result = {}
    
    # 如果没有提供keys,返回所有数据
    if not keys:
        return self._data
        
    # 处理提供的keys
    for key in keys:
        if isinstance(key, int):
            # 处理索引
            if key < 0 or key >= len(self._data):
                raise IndexError(f"Index {key} is out of range")
            field_name = list(self._data.keys())[key]
            result[field_name] = self._data[field_name]
        else:
            # 处理键名
            result[key] = self._data.get(key, None)
            
    return result