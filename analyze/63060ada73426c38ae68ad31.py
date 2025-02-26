def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    for key, value in values_dict.items():
        if value.isdigit():
            values_dict[key] = int(value)
        else:
            try:
                # Attempt to convert to float if possible
                values_dict[key] = float(value)
            except ValueError:
                # Keep as string if conversion fails
                values_dict[key] = value