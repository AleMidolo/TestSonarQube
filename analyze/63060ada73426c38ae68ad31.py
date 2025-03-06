def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    if parser_name == "main":
        for key, value in values_dict.items():
            if value.isdigit():
                values_dict[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            elif value.lower() in ('true', 'false'):
                values_dict[key] = value.lower() == 'true'
    elif parser_name == "virsh":
        for key, value in values_dict.items():
            if key == "memory":
                values_dict[key] = int(value)
            elif key == "vcpu":
                values_dict[key] = int(value)
            elif key == "autostart":
                values_dict[key] = value.lower() == 'true'
    elif parser_name == "ospd":
        for key, value in values_dict.items():
            if key == "port":
                values_dict[key] = int(value)
            elif key == "timeout":
                values_dict[key] = float(value)
            elif key == "verbose":
                values_dict[key] = value.lower() == 'true'
    # Add more parser-specific conversions as needed