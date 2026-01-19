def __setitem__(self, key, value):
    """
    Establece el valor correspondiente a la clave al valor especificado
    :param key:str
    :param value:str, el valor especificado
    :return:None
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__setitem__('first_name', 'nuevo nombre')
    camelize_map['first_name'] = 'nuevo nombre'
    """
    # Convert snake_case key to camelCase
    def snake_to_camel(snake_str):
        components = snake_str.split('_')
        # Keep the first component as is, capitalize the rest
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = snake_to_camel(key)
    # Store the value using the camelCase key in the internal dictionary
    super().__setitem__(camel_key, value)
    print(f"camelize_map['{key}'] = '{value}'")