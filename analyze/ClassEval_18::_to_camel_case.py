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
    if not key:
        return key
    parts = key.split('_')
    result = parts[0].lower()
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:].lower()
    return result