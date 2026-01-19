def __setitem__(self, key, value):
    """
        Establece el valor correspondiente a la clave al valor especificado
        :param key:str
        :param value:str, el valor especificado
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'nuevo nombre')
        camelize_map['first_name'] = 'nuevo nombre'
        """
    self._data[self._convert_key(key)] = value