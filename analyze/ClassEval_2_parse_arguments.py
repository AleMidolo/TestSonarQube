def parse_arguments(self, command_string):
    """
        解析给定的命令行参数字符串，并调用 _convert_type 将解析结果存储在参数字典中的特定类型中。
        检查是否缺少必需的参数，如果有，则返回 False 和缺失的参数名称，否则返回 True。
        :param command_string: str, 命令行参数字符串，格式为 "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) 如果解析成功，(False, missing_args) 如果解析失败，
            其中 missing_args 是缺失参数名称的集合，类型为字符串。
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
    args = command_string.split()
    for arg in args[1:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
        else:
            key = arg
            value = True
        key = key.lstrip('-')
        if key in self.types:
            self.arguments[key] = self._convert_type(key, value)
        else:
            self.arguments[key] = value
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)