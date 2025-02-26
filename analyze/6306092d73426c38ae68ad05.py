def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.
    """
    # Assuming there's a dictionary that holds the command specifications
    command_specs = {
        'command1': {'option1': 'spec1', 'option2': 'spec2'},
        'command2': {'option1': 'spec3', 'option3': 'spec4'},
    }
    
    # Retrieve the command specification
    command_spec = command_specs.get(command_name)
    
    if command_spec is None:
        return None  # Command not found
    
    # Retrieve the option specification
    option_spec = command_spec.get(argument_name)
    
    return option_spec  # Return the option specification or None if not found