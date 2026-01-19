def __getitem__(self, key):
    """
        Devuelve el valor correspondiente a la clave
        :param key:str
        :return:str, el valor correspondiente a la clave
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """
    return self._data[self._convert_key(key)]