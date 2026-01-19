def __getitem__(self, key):
    """
    Devuelve el valor correspondiente a la clave
    :param key:str
    :return:str, el valor correspondiente a la clave
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__getitem__('first_name')
    'John'
    """
    # Convert snake_case key to camelCase
    def snake_to_camel(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = snake_to_camel(key)
    return self.__dict__[camel_key]