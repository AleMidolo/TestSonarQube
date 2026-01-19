def __setitem__(self, key, value):
    """
    Set the value corresponding to the key to the specified value
    :param key:str
    :param value:str, the specified value
    :return:None
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__setitem__('first_name', 'new name')
    camelize_map['first_name'] = 'new name'
    """
    # Convert snake_case key to camelCase
    parts = key.split('_')
    camel_key = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    # Set the value using the camelCase key in the underlying dict
    dict.__setitem__(self, camel_key, value)