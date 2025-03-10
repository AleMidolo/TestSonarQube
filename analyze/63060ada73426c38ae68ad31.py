def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
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
        if "active" in values_dict:
            values_dict["active"] = values_dict["active"].lower() == "true"
    
    elif parser_name == "ospd":
        if "threads" in values_dict:
            values_dict["threads"] = int(values_dict["threads"])
        if "debug" in values_dict:
            values_dict["debug"] = values_dict["debug"].lower() == "true"
    
    # Puedes agregar más conversiones para otros comandos aquí.
    
    return values_dict