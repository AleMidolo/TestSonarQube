def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    if not hasattr(self, '_option_specs'):
        return None
    
    command_specs = self._option_specs.get(command_name, {})
    return command_specs.get(argument_name, None)