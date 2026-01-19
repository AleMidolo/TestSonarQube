@staticmethod
def _to_camel_case(key):
    """
        Formatea la llave a camel case
        :param key:str
        :return:str, cadena de clave convertida
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
    components = key.split('_')
    return components[0] + ''.join((x.title() for x in components[1:]))