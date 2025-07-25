def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    # Get parser options for this command
    parser_options = self.parser_options.get(parser_name, {})

    # Iterate through all arguments
    for arg_name, value in values_dict.items():
        # Skip if value is None or empty
        if value is None or value == '':
            continue
            
        # Get type from parser options if exists
        arg_type = parser_options.get(arg_name, {}).get('type', str)
        
        try:
            # Handle boolean values
            if arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
            # Handle lists
            elif arg_type == list:
                if isinstance(value, str):
                    values_dict[arg_name] = value.split(',')
            # Handle integers
            elif arg_type == int:
                values_dict[arg_name] = int(value)
            # Handle floats
            elif arg_type == float:
                values_dict[arg_name] = float(value)
            # All other types
            else:
                values_dict[arg_name] = arg_type(value)
                
        except (ValueError, TypeError):
            # If conversion fails, keep original value
            continue