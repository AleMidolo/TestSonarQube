def __setitem__(self, key, value):
    """
        Imposta il valore corrispondente alla chiave al valore specificato
        :param key:str
        :param value:str, il valore specificato
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'new name')
        camelize_map['first_name'] = 'new name'
        """
    self._data[self._convert_key(key)] = value