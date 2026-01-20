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
    
    # Try to get the value using the camelCase key from the internal dictionary
    # Assuming the class has an internal dictionary attribute (e.g., self._data or self.__dict__)
    if hasattr(self, '_data'):
        return self._data[camel_key]
    else:
        return self.__dict__[camel_key]