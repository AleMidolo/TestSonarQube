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
    # Convert snake_case key to camelCase
    camel_key = self._to_camel_case(key)
    # Return the value from the internal dictionary
    return self._data[camel_key]