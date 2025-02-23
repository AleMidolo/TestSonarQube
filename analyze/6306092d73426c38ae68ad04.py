def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    command_options = {
        'main': ['--help', '--version'],
        'virsh': ['--connect', '--list'],
        'ospd': ['--start', '--stop']
    }
    
    return command_options.get(command_name, [])