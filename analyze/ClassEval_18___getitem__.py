def __getitem__(self, key):
    """
    返回与键对应的值
    :param key:str
    :return:str, 与键对应的值
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__getitem__('first_name')
    'John'
    """
    # Convert snake_case key to camelCase
    camel_key = self._to_camel_case(key)
    # Try to get the value using the camelCase key from internal storage
    return self._data[camel_key]

def _to_camel_case(self, snake_str):
    """
    Convert snake_case string to camelCase
    """
    components = snake_str.split('_')
    # Keep the first component as is, capitalize the rest
    return components[0] + ''.join(x.title() for x in components[1:])