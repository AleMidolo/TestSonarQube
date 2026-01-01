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
    import re
    parts = re.split('\\s+', command_string)
    parts = parts[2:]
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            key = key.lstrip('-')
            self.arguments[key] = self._convert_type(key, value)
        else:
            key = part.lstrip('-')
            if key in self.types:
                self.arguments[key] = True
            else:
                self.arguments[key] = True
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)