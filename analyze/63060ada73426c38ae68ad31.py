def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Converte gli argomenti nei tipi corretti modificando il parametro values_dict.

    Per impostazione predefinita, tutti i valori sono stringhe.

    :param parser_name: Il nome del comando, ad esempio main, virsh, ospd, ecc.
    :param values_dict: Il dizionario con gli argomenti
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            # Try to convert to int
            try:
                values_dict[key] = int(value)
                continue
            except ValueError:
                pass
            
            # Try to convert to float
            try:
                values_dict[key] = float(value)
                continue
            except ValueError:
                pass
            
            # Try to convert to boolean
            if value.lower() in ('true', 'false'):
                values_dict[key] = value.lower() == 'true'
                continue
            
            # Try to convert to list if the value contains commas
            if ',' in value:
                values_dict[key] = value.split(',')
                continue
            
            # Try to convert to dict if the value is in JSON format
            if value.startswith('{') and value.endswith('}'):
                try:
                    import json
                    values_dict[key] = json.loads(value)
                    continue
                except json.JSONDecodeError:
                    pass