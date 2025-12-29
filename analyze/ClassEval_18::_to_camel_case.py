@staticmethod
def _to_camel_case(key):
    """
        converte la stringa key in camel case
        :param key:str
        :return:str, stringa key convertita
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
    if not key or '_' not in key:
        return key
    parts = key.split('_')
    return parts[0] + ''.join((part.capitalize() for part in parts[1:]))