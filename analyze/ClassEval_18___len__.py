def __len__(self):
    """
    返回自身数据的长度
    :return:int，数据的长度
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map['last_name'] = 'Doe'
    >>> camelize_map['age'] = 30
    >>> camelize_map.__len__()
    3
    """
    return len(self.__dict__)