def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    # Get parser configuration for this command
    parser_config = self.parsers.get(parser_name, {})
    
    # Iterate through all arguments in values_dict
    for arg_name, value in values_dict.items():
        # Skip if value is None
        if value is None:
            continue
            
        # Get argument type from parser config if it exists
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        try:
            # Convert boolean string values
            if arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 'yes', '1', 'on')
            # Convert numeric types        
            elif arg_type in (int, float):
                values_dict[arg_name] = arg_type(value)
            # Convert lists
            elif arg_type == list and isinstance(value, str):
                values_dict[arg_name] = value.split(',')
                
        except (ValueError, TypeError):
            # If conversion fails, keep original string value
            continue