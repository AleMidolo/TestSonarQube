def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    if parser_name == "main":
        if "timeout" in values_dict:
            values_dict["timeout"] = int(values_dict["timeout"])
        if "verbose" in values_dict:
            values_dict["verbose"] = bool(values_dict["verbose"])
        if "retries" in values_dict:
            values_dict["retries"] = int(values_dict["retries"])
    
    elif parser_name == "virsh":
        if "memory" in values_dict:
            values_dict["memory"] = int(values_dict["memory"])
        if "cpu" in values_dict:
            values_dict["cpu"] = int(values_dict["cpu"])
        if "active" in values_dict:
            values_dict["active"] = values_dict["active"].lower() == "true"
    
    elif parser_name == "ospd":
        if "port" in values_dict:
            values_dict["port"] = int(values_dict["port"])
        if "ssl" in values_dict:
            values_dict["ssl"] = values_dict["ssl"].lower() == "true"
        if "timeout" in values_dict:
            values_dict["timeout"] = float(values_dict["timeout"])
    
    # Add more parser-specific conversions as needed