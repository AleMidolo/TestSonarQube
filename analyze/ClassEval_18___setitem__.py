def __setitem__(self, key, value):
    """
        将与键对应的值设置为指定的值
        :param key:str
        :param value:str，指定的值
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'new name')
        camelize_map['first_name'] = 'new name'
        """
    self._data[self._convert_key(key)] = value