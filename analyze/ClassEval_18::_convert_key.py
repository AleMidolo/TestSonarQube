def _convert_key(self, key):
    """
        将键字符串转换为驼峰式
        :param key:str
        :return:str, 转换后的键字符串
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """
    return self._to_camel_case(key)