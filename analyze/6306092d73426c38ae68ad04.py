def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
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
            
        # Get option strings (both short and long forms)
        opt_strings = action.option_strings
        
        # Get option type
        opt_type = action.type.__name__ if action.type else 'str'
        
        # Get default value
        default = action.default
        
        # Get help text
        help_text = action.help
        
        # Get if option is required
        required = action.required
        
        # Create option spec dictionary
        option_spec = {
            'name': opt_strings,
            'type': opt_type,
            'default': default,
            'help': help_text,
            'required': required
        }
        
        # Add to options list
        options.append(option_spec)
        
    return options