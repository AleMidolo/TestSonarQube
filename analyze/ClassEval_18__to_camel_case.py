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
    parts = key.split('_')
    return parts[0] + ''.join((word.capitalize() for word in parts[1:]))