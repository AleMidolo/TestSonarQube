def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    # Check if command exists in command specs
    if command_name not in self.command_specs:
        return None
        
    # Get command spec
    command_spec = self.command_specs[command_name]
    
    # Check if argument exists in command's arguments
    if 'arguments' not in command_spec or argument_name not in command_spec['arguments']:
        return None
        
    # Return the argument specification
    return command_spec['arguments'][argument_name]