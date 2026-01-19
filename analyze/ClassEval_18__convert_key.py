def _convert_key(self, key):
    """
        converte la stringa della key in camel case
        :param key:str
        :return:str, stringa della chiave convertita
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """
    return self._to_camel_case(key)