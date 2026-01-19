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
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = to_camel_case(key)
    self.__dict__[camel_key] = value