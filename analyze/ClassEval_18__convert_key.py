def _convert_key(self, key):
    """
    converte la stringa della key in camel case
    :param key:str
    :return:str, stringa della chiave convertita
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map._convert_key('first_name')
    'firstName'
    """
    parts = key.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])