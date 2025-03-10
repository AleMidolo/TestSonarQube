def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    # Assuming self.parser is an ArgumentParser or similar object
    if command_name in self.parser._actions:
        return [action.option_strings for action in self.parser._actions if action.option_strings]
    else:
        return []