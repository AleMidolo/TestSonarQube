def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    # Get the command spec from the command registry
    command_spec = self.commands.get(command_name)
    if not command_spec:
        return None
        
    # Look for the argument in the command's options
    if 'options' in command_spec:
        for option in command_spec['options']:
            if option['name'] == argument_name:
                return option
                
    return None