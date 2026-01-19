@staticmethod
def _to_camel_case(key):
    """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
    parts = key.split('_')
    return parts[0] + ''.join((part.capitalize() for part in parts[1:]))