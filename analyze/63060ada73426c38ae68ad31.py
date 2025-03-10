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
        elif value.replace('.', '', 1).isdigit():
            values_dict[key] = float(value)
        elif value.lower() in ('true', 'false'):
            values_dict[key] = value.lower() == 'true'
        else:
            # Si no es un número ni un booleano, se deja como string
            pass