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
        if token.startswith('--'):
            if '=' in token:
                key_value = token[2:].split('=', 1)
                key = key_value[0]
                value = key_value[1]
                converted_value = self._convert_type(key, value)
                self.arguments[key] = converted_value
            else:
                key = token[2:]
                self.arguments[key] = True
        elif token.startswith('-') and (not token.startswith('--')):
            key = token[1:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                value = tokens[i + 1]
                converted_value = self._convert_type(key, value)
                self.arguments[key] = converted_value
                i += 1
            else:
                self.arguments[key] = True
        i += 1
    missing_args = set()
    for req_arg in self.required:
        if req_arg not in self.arguments:
            missing_args.add(req_arg)
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)