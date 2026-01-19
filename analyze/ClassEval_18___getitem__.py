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
    
    # Try to get the value using the camelCase key from internal storage
    if hasattr(self, '_data'):
        return self._data.get(camel_key)
    
    # Alternative: if using __dict__ directly
    return self.__dict__.get(camel_key)