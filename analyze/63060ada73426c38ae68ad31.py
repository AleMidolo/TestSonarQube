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
            else:
                try:
                    values_dict[key] = float(value)
                except ValueError:
                    pass  # Leave as string if conversion fails