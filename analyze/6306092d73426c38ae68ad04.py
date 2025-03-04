def get_parser_option_specs(self, command_name):
    """
    Gets all the options for the specified command

    :param command_name: the command name (main, virsh, ospd, etc...)
    :return: the list of all command options
    """
    # Get the parser for the specified command
    parser = self.get_parser(command_name)
    
    # Initialize empty list to store options
    options = []
    
    # Iterate through all parser actions to get options
    for action in parser._actions:
        # Skip help action
        if isinstance(action, argparse._HelpAction):
            continue
            
        # Get option strings (both short and long forms)
        option_strings = action.option_strings
        
        # Get option details
        option_spec = {
            'name': action.dest,
            'flags': option_strings,
            'help': action.help,
            'default': action.default,
            'required': action.required,
            'type': str(action.type) if action.type else None,
            'choices': action.choices,
            'metavar': action.metavar
        }
        
        options.append(option_spec)
        
    return options