def __getitem__(self, key):
    """
    Return the value corresponding to the key
    :param key:str
    :return:str,the value corresponding to the key
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__getitem__('first_name')
    'John'
    """
    # Convert snake_case key to camelCase
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = to_camel_case(key)
    
    # Try to get the value using the camelCase key
    if hasattr(self, '_data'):
        return self._data.get(camel_key)
    else:
        # Fallback to object attribute access
        return getattr(self, camel_key)