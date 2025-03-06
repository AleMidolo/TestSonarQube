def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.

    Args:
        command_name (str): The name of the command.
        argument_name (str): The name of the argument.

    Returns:
        dict: The specification for the specified option name.
    """
    if not hasattr(self, '_command_specs'):
        return None
    
    command_spec = self._command_specs.get(command_name)
    if not command_spec:
        return None
    
    for option_spec in command_spec.get('options', []):
        if option_spec.get('name') == argument_name:
            return option_spec
    
    return None