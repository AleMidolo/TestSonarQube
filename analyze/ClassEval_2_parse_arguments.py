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
    # Split the command string into tokens
    tokens = command_string.split()
    
    # Skip the first two tokens (python script.py)
    tokens = tokens[2:] if len(tokens) > 2 else []
    
    # Initialize arguments dictionary
    self.arguments = {}
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Check if token starts with -- or -
        if token.startswith('--') or token.startswith('-'):
            # Remove leading dashes
            arg_name = token.lstrip('-')
            
            # Check if argument has = sign (e.g., --arg1=value1)
            if '=' in arg_name:
                parts = arg_name.split('=', 1)
                arg_name = parts[0]
                value = parts[1]
                self.arguments[arg_name] = self._convert_type(arg_name, value)
                i += 1
            else:
                # Check if next token exists and is not an argument
                if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                    # Next token is the value
                    value = tokens[i + 1]
                    self.arguments[arg_name] = self._convert_type(arg_name, value)
                    i += 2
                else:
                    # It's a flag/option (boolean)
                    self.arguments[arg_name] = True
                    i += 1
        else:
            i += 1
    
    # Check for missing required arguments
    missing_args = set()
    if hasattr(self, 'required_args'):
        for req_arg in self.required_args:
            if req_arg not in self.arguments:
                missing_args.add(req_arg)
    
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)