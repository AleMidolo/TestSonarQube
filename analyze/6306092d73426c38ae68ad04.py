def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    # Assuming the options are stored in a dictionary where the key is the command name
    # and the value is a list of options.
    command_options = {
        "main": ["--help", "--version", "--verbose"],
        "virsh": ["--connect", "--list", "--details"],
        "ospd": ["--config", "--log-level", "--output"]
    }
    
    # Return the list of options for the specified command
    return command_options.get(command_name, [])