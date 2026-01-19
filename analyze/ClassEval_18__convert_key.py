def _convert_key(self, key):
    """
    将键字符串转换为驼峰式
    :param key:str
    :return:str, 转换后的键字符串
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map._convert_key('first_name')
    'firstName'
    """
    components = key.split('_')
    # 第一个组件保持小写,其余组件首字母大写
    return components[0] + ''.join(word.capitalize() for word in components[1:])