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
    
    # Iterate through all options in the parser
    for action in parser._actions:
        # Skip help action
        if isinstance(action, argparse._HelpAction):
            continue
            
        # Get option names (both short and long forms)
        option_names = action.option_strings
        
        # Get option properties
        option_spec = {
            'names': option_names,
            'help': action.help,
            'default': action.default,
            'required': action.required,
            'type': action.type.__name__ if action.type else None,
            'choices': action.choices,
            'dest': action.dest
        }
        
        options.append(option_spec)
        
    return options