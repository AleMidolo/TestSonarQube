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
    
    # Split command string into tokens
    tokens = command_string.split()
    
    # Skip "python script.py" part
    i = 0
    while i < len(tokens) and not tokens[i].startswith('-'):
        i += 1
    
    # Parse arguments
    while i < len(tokens):
        token = tokens[i]
        
        # Remove leading dashes
        arg_name = token.lstrip('-')
        
        # Check if it's in format --arg=value
        if '=' in arg_name:
            parts = arg_name.split('=', 1)
            key = parts[0]
            value = parts[1]
            self.arguments[key] = self._convert_type(value)
            i += 1
        else:
            # Check if next token exists and is not an argument
            if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                # It's a key-value pair
                key = arg_name
                value = tokens[i + 1]
                self.arguments[key] = self._convert_type(value)
                i += 2
            else:
                # It's a boolean flag
                self.arguments[arg_name] = True
                i += 1
    
    # Check for missing required arguments
    if hasattr(self, 'required_args'):
        missing_args = set()
        for required_arg in self.required_args:
            if required_arg not in self.arguments:
                missing_args.add(required_arg)
        
        if missing_args:
            return (False, missing_args)
    
    return (True, None)