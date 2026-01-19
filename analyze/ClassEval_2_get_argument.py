def get_argument(self, key):
    """
    从参数字典中检索指定参数的值并返回。
    :param key: str, 参数名称
    :return: 参数的值，如果参数不存在则返回 None。
    >>> parser.arguments
    {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
    >>> parser.get_argument('arg2')
    'value2'
    """
    return self.arguments.get(key)