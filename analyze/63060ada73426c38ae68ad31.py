def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Casts arguments to correct types by modifying values_dict param.

    By default all the values are strings.

    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments
    """
    if parser_name == "main":
        if "port" in values_dict:
            values_dict["port"] = int(values_dict["port"])
        if "timeout" in values_dict:
            values_dict["timeout"] = float(values_dict["timeout"])
        if "verbose" in values_dict:
            values_dict["verbose"] = values_dict["verbose"].lower() == "true"
    
    elif parser_name == "virsh":
        if "memory" in values_dict:
            values_dict["memory"] = int(values_dict["memory"])
        if "cpu" in values_dict:
            values_dict["cpu"] = int(values_dict["cpu"])
        if "autostart" in values_dict:
            values_dict["autostart"] = values_dict["autostart"].lower() == "true"
    
    elif parser_name == "ospd":
        if "threads" in values_dict:
            values_dict["threads"] = int(values_dict["threads"])
        if "debug" in values_dict:
            values_dict["debug"] = values_dict["debug"].lower() == "true"
    
    # Add more parser-specific conversions as needed