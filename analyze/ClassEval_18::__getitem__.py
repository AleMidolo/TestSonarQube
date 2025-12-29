def __getitem__(self, key):
    """
        返回与键对应的值
        :param key:str
        :return:str, 与键对应的值
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """
    return self._data[self._convert_key(key)]