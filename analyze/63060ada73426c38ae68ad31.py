def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Converte gli argomenti nei tipi corretti modificando il parametro values_dict.

    Per impostazione predefinita, tutti i valori sono stringhe.

    :param parser_name: Il nome del comando, ad esempio main, virsh, ospd, ecc.
    :param values_dict: Il dizionario con gli argomenti
    """
    if not values_dict:
        return

    # Get parser configuration for this command
    parser_config = self.parsers.get(parser_name, {})
    
    # Iterate through all arguments in values_dict
    for arg_name, value in values_dict.items():
        # Skip if value is None
        if value is None:
            continue
            
        # Get argument type from parser config
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        try:
            # Convert boolean strings
            if arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
            # Convert numeric types
            elif arg_type in (int, float):
                values_dict[arg_name] = arg_type(value)
            # Convert lists
            elif arg_type == list and isinstance(value, str):
                values_dict[arg_name] = value.split(',')
            # Convert other types
            else:
                values_dict[arg_name] = arg_type(value)
                
        except (ValueError, TypeError):
            # Keep original value if conversion fails
            continue