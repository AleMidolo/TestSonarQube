def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    if command_name == "main":
        return [
            {"name": "--help", "action": "store_true", "help": "show this help message and exit"},
            {"name": "--version", "action": "store_true", "help": "show program's version number and exit"},
        ]
    elif command_name == "virsh":
        return [
            {"name": "--connect", "type": str, "help": "connect to hypervisor"},
            {"name": "--list", "action": "store_true", "help": "list domains"},
        ]
    elif command_name == "ospd":
        return [
            {"name": "--config", "type": str, "help": "path to configuration file"},
            {"name": "--log-level", "type": str, "help": "set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"},
        ]
    else:
        return []