def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    # Obtener la configuración del parser
    parser_config = self.config.get(parser_name, {})
    
    # Iterar sobre los argumentos en values_dict
    for arg_name, value in values_dict.items():
        # Obtener el tipo definido en la configuración
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        # Ignorar si el valor es None
        if value is None:
            continue
            
        try:
            # Convertir listas
            if isinstance(value, list):
                values_dict[arg_name] = [arg_type(v) for v in value]
            # Convertir valores individuales
            else:
                # Manejar booleanos especialmente
                if arg_type == bool:
                    if isinstance(value, str):
                        values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
                    else:
                        values_dict[arg_name] = bool(value)
                else:
                    values_dict[arg_name] = arg_type(value)
                    
        except (ValueError, TypeError):
            # Si falla la conversión, dejar el valor original
            continue