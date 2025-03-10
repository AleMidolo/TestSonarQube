def get_option_spec(self, command_name, argument_name):
    """
    Gets the specification for the specified option name.

    Args:
        command_name (str): The name of the command.
        argument_name (str): The name of the argument.

    Returns:
        dict: The specification for the specified option name.
    """
    # Assuming self.options is a dictionary where keys are command names
    # and values are dictionaries of argument specifications
    if command_name in self.options:
        if argument_name in self.options[command_name]:
            return self.options[command_name][argument_name]
    return None