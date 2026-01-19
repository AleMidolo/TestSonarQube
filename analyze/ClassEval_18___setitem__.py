def __setitem__(self, key, value):
    """
    将与键对应的值设置为指定的值
    :param key:str
    :param value:str，指定的值
    :return:None
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__setitem__('first_name', 'new name')
    camelize_map['first_name'] = 'new name'
    """
    # Convert snake_case key to camelCase
    def snake_to_camel(snake_str):
        components = snake_str.split('_')
        # Keep the first component as is, capitalize the rest
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = snake_to_camel(key)
    # Store the value using the camelCase key in the internal dictionary
    self.__dict__[camel_key] = value