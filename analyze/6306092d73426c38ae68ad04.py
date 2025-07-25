def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    # Assuming self.parser is an ArgumentParser or similar object
    if command_name not in self.parser._actions_by_dest:
        return []
    
    options = []
    for action in self.parser._actions:
        if action.dest == command_name:
            options.extend(action.option_strings)
    
    return options