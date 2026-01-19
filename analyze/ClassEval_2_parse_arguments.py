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
    # Initialize arguments dictionary if not exists
    if not hasattr(self, 'arguments'):
        self.arguments = {}
    
    # Split the command string into tokens
    tokens = command_string.split()
    
    # Skip the first two tokens (python script.py)
    if len(tokens) >= 2:
        tokens = tokens[2:]
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Check if token starts with -- or -
        if token.startswith('--') or token.startswith('-'):
            # Remove leading dashes
            arg_name = token.lstrip('-')
            
            # Check if it's in format --arg=value
            if '=' in arg_name:
                parts = arg_name.split('=', 1)
                arg_name = parts[0]
                value = parts[1]
                # Convert type if _convert_type method exists
                if hasattr(self, '_convert_type'):
                    value = self._convert_type(arg_name, value)
                self.arguments[arg_name] = value
                i += 1
            else:
                # Check if next token exists and is not an argument
                if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                    value = tokens[i + 1]
                    # Convert type if _convert_type method exists
                    if hasattr(self, '_convert_type'):
                        value = self._convert_type(arg_name, value)
                    self.arguments[arg_name] = value
                    i += 2
                else:
                    # It's a flag/option (boolean)
                    self.arguments[arg_name] = True
                    i += 1
        else:
            i += 1
    
    # Check for missing required arguments
    if hasattr(self, 'required_args'):
        missing_args = set()
        for req_arg in self.required_args:
            if req_arg not in self.arguments:
                missing_args.add(req_arg)
        
        if missing_args:
            return (False, missing_args)
    
    return (True, None)