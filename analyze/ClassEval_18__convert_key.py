def _convert_key(self, key):
    """
    Formatea la llave a camel case
    :param key:str
    :return:str, cadena de clave convertida
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map._convert_key('first_name')
    'firstName'
    """
    components = key.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])