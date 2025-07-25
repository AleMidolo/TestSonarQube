def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    # Get the parser for the specified command
    parser = self.parsers.get(command_name)
    
    if not parser:
        return []
        
    # Initialize empty list to store options
    options = []
    
    # Get all options from the parser
    for action in parser._actions:
        # Skip help action
        if isinstance(action, argparse._HelpAction):
            continue
            
        # Get option strings (both short and long forms)
        opt_strings = action.option_strings
        
        # Get option details
        option_spec = {
            'name': action.dest,
            'flags': opt_strings,
            'help': action.help,
            'default': action.default,
            'required': action.required,
            'type': str(action.type) if action.type else None,
            'choices': action.choices,
            'nargs': action.nargs
        }
        
        options.append(option_spec)
        
    return options