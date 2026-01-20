def __delitem__(self, key):
    """
    Elimina el valor correspondiente a la clave
    :param key:str
    :return:None
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__delitem__('first_name')
    >>> flag = 'first_name' in camelize_map
    flag = False
    """
    camelized_key = self._camelize(key)
    del self._data[camelized_key]