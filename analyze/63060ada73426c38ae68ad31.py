def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            # Convertir a int si es posible
            if value.isdigit():
                values_dict[key] = int(value)
            # Convertir a float si es posible
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            # Convertir a booleano si es posible
            elif value.lower() in ['true', 'false']:
                values_dict[key] = value.lower() == 'true'
            # Convertir a None si es 'None'
            elif value.lower() == 'none':
                values_dict[key] = None
    return values_dict