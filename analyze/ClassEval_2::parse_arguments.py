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
    pattern = '(--\\w+|-\\w+)(=([^ ]+)|\\s+([^ ]+))?'
    matches = re.findall(pattern, command_string)
    missing_args = set()
    for match in matches:
        arg_name = match[0].lstrip('-')
        value = match[2] if match[2] else match[3] if match[3] else True
        if arg_name in self.types:
            value = self._convert_type(arg_name, value)
        self.arguments[arg_name] = value
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)