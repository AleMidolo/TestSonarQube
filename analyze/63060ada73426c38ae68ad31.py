def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Converte gli argomenti nei tipi corretti modificando il parametro values_dict.

    Per impostazione predefinita, tutti i valori sono stringhe.

    :param parser_name: Il nome del comando, ad esempio main, virsh, ospd, ecc.
    :param values_dict: Il dizionario con gli argomenti
    """
    # Get parser configuration for this command
    parser_config = self.parsers.get(parser_name, {})
    
    # Iterate through all arguments in values_dict
    for arg_name, value in values_dict.items():
        # Get argument type from parser config if it exists
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        try:
            # Skip conversion if value is None or already correct type
            if value is None or isinstance(value, arg_type):
                continue
                
            # Convert boolean strings
            if arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
                else:
                    values_dict[arg_name] = bool(value)
                    
            # Convert numbers
            elif arg_type in (int, float):
                values_dict[arg_name] = arg_type(value)
                
            # Convert lists
            elif arg_type == list:
                if isinstance(value, str):
                    values_dict[arg_name] = value.split(',')
                elif not isinstance(value, list):
                    values_dict[arg_name] = list(value)
                    
        except (ValueError, TypeError):
            # If conversion fails, keep original value
            continue