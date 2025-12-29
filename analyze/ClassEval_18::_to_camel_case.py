@staticmethod
def _to_camel_case(key):
    """
        将键字符串转换为驼峰式
        :param key:str
        :return:str, 转换后的键字符串
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
    if not key:
        return key
    parts = key.split('_')
    return parts[0] + ''.join((part.capitalize() for part in parts[1:]))