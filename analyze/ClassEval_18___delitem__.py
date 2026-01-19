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
    # Convert the key to camelCase format
    camel_key = self._to_camel_case(key)
    # Delete the item from the internal dictionary
    del self._data[camel_key]