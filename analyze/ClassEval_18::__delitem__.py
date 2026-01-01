def __delitem__(self, key):
    """
        Elimina il valore corrispondente alla chiave
        :param key:str
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__delitem__('first_name')
        >>> flag = 'first_name' in camelize_map
        flag = False
        """
    del self._data[self._convert_key(key)]