def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
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