def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Converte gli argomenti nei tipi corretti modificando il parametro values_dict.

    Per impostazione predefinita, tutti i valori sono stringhe.

    :param parser_name: Il nome del comando, ad esempio main, virsh, ospd, ecc.
    :param values_dict: Il dizionario con gli argomenti
    """
    if not values_dict:
        return

    # Get parser options for this command
    parser_options = self.parsers.get(parser_name, {}).get('options', {})

    for arg_name, value in values_dict.items():
        # Skip if argument not in parser options
        if arg_name not in parser_options:
            continue
            
        arg_type = parser_options[arg_name].get('type')
        
        # Convert value based on type
        if arg_type == 'bool':
            if isinstance(value, str):
                values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
        elif arg_type == 'int':
            try:
                values_dict[arg_name] = int(value)
            except (ValueError, TypeError):
                pass
        elif arg_type == 'float':
            try:
                values_dict[arg_name] = float(value)
            except (ValueError, TypeError):
                pass
        elif arg_type == 'list':
            if isinstance(value, str):
                values_dict[arg_name] = value.split(',')