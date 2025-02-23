def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    command_options = {
        'main': ['--help', '--version', '--verbose'],
        'virsh': ['--connect', '--list', '--start'],
        'ospd': ['--config', '--debug', '--status']
    }
    
    return command_options.get(command_name, [])