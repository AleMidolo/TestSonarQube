def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Converte gli argomenti nei tipi corretti modificando il parametro values_dict.

    Per impostazione predefinita, tutti i valori sono stringhe.

    :param parser_name: Il nome del comando, ad esempio main, virsh, ospd, ecc.
    :param values_dict: Il dizionario con gli argomenti
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            if value.lower() == 'true':
                values_dict[key] = True
            elif value.lower() == 'false':
                values_dict[key] = False
            elif value.isdigit():
                values_dict[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            elif value.lower() == 'none':
                values_dict[key] = None
    return values_dict