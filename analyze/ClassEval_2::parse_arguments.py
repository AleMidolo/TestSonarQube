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
    self.arguments = {}
    tokens = command_string.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.startswith('--') and '=' in token:
            arg_name = token[2:].split('=')[0]
            arg_value = token.split('=', 1)[1]
            self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
            i += 1
        elif token.startswith('--'):
            arg_name = token[2:]
            self.arguments[arg_name] = True
            i += 1
        elif token.startswith('-') and len(token) > 1 and (not token.startswith('--')):
            arg_name = token[1:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                arg_value = tokens[i + 1]
                self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                i += 2
            else:
                self.arguments[arg_name] = True
                i += 1
        else:
            i += 1
    missing_args = self.required - set(self.arguments.keys())
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)