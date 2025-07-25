def get_parser_option_specs(self, command_name):
    """
    Ottiene tutte le opzioni per il comando specificato

    :param command_name: il nome del comando (main, virsh, ospd, ecc...)
    :return: la lista di tutte le opzioni del comando
    """
    # Initialize empty list to store options
    options = []
    
    # Get the parser for the specified command
    parser = self.parsers.get(command_name)
    
    if parser is None:
        return options
        
    # Get all options from the parser
    for action in parser._actions:
        # Skip help action
        if isinstance(action, argparse._HelpAction):
            continue
            
        # Get option names (both short and long forms)
        option_names = action.option_strings
        
        # Get option details
        option_spec = {
            'names': option_names,
            'help': action.help,
            'required': action.required,
            'default': action.default,
            'type': str(action.type.__name__) if action.type else None,
            'choices': action.choices,
            'dest': action.dest
        }
        
        options.append(option_spec)
        
    return options