def __delitem__(self, key):
    """
    Delete the value corresponding to the key
    :param key:str
    :return:None
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__delitem__('first_name')
    >>> flag = 'first_name' in camelize_map
    flag = False
    """
    # Convert snake_case key to camelCase
    camel_key = self._to_camel_case(key)
    # Delete from the internal dictionary
    del self._data[camel_key]