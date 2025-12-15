class ArgumentParser: 
    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        >>> parser.arguments
        {'key1': 'value1', 'option1': True}
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'type1'}
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
        return self.arguments.get(key)
    
    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it wull be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type:str, Argument type, default is str
        >>> parser.add_argument('arg1', True, 'int')
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'int'}
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type
    
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value
    
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
                key, value = arg.split('=')
                key = key.lstrip('--')
            else:
                key = arg.lstrip('-')
                value = True
            
            if key in self.types:
                self.arguments[key] = self._convert_type(key, value)
            else:
                self.arguments[key] = value
        
        missing_args = self.required - self.arguments.keys()
        if missing_args:
            return False, missing_args
        return True, None