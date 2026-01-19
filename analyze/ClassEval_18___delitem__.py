def __delitem__(self, key):
    """
    删除与键对应的值
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

def _to_camel_case(self, snake_str):
    """
    Convert snake_case string to camelCase
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])