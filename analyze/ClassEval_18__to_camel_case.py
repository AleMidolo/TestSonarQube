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
    components = key.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])