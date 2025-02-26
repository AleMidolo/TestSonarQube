def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    # Assuming there's a dictionary that holds command specifications
    command_specs = {
        'command1': {'option1': {'type': 'string', 'required': True}},
        'command2': {'option2': {'type': 'int', 'required': False}},
    }
    
    # Retrieve the command specification
    command_spec = command_specs.get(command_name)
    
    if command_spec:
        # Retrieve the option specification
        option_spec = command_spec.get(argument_name)
        return option_spec
    
    return None