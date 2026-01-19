def parse_arguments(self, command_string):
    """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
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
        if token.startswith('-'):
            arg_name = token.lstrip('-')
            if '=' in arg_name:
                arg_name, value = arg_name.split('=', 1)
                converted_value = self._convert_type(arg_name, value)
                self.arguments[arg_name] = converted_value
            elif i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                value = tokens[i + 1]
                converted_value = self._convert_type(arg_name, value)
                self.arguments[arg_name] = converted_value
                i += 1
            else:
                self.arguments[arg_name] = True
        i += 1
    missing_args = self.required - set(self.arguments.keys())
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)