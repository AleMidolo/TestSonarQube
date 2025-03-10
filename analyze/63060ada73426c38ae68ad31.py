def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    if parser_name == "main":
        for key, value in values_dict.items():
            if key == "port":
                values_dict[key] = int(value)
            elif key == "verbose":
                values_dict[key] = bool(value)
            elif key == "timeout":
                values_dict[key] = float(value)
    elif parser_name == "virsh":
        for key, value in values_dict.items():
            if key == "memory":
                values_dict[key] = int(value)
            elif key == "cpu":
                values_dict[key] = int(value)
            elif key == "active":
                values_dict[key] = bool(value)
    elif parser_name == "ospd":
        for key, value in values_dict.items():
            if key == "threads":
                values_dict[key] = int(value)
            elif key == "debug":
                values_dict[key] = bool(value)
            elif key == "interval":
                values_dict[key] = float(value)
    # Add more parser-specific conversions as needed
    return values_dict