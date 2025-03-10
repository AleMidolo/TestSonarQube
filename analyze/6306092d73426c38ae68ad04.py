def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    if command_name == "main":
        return ["--help", "--version", "--verbose"]
    elif command_name == "virsh":
        return ["--connect", "--list", "--details"]
    elif command_name == "ospd":
        return ["--config", "--log-level", "--output"]
    else:
        return []