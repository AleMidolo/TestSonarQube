def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
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