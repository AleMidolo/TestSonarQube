def __getitem__(self, key):
        """
        Restituisce il valore corrispondente alla chiave
        :param key:str
        :return:str, il valore corrispondente alla chiave
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """
        return self._data[self._convert_key(key)]