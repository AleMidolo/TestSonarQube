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
        # Obtener la configuración del argumento específico
        arg_config = parser_config.get(arg_name, {})
        
        # Si el valor es None o vacío, continuar
        if value is None or value == '':
            continue
            
        # Obtener el tipo del argumento de la configuración
        arg_type = arg_config.get('type', str)
        
        try:
            # Convertir listas
            if isinstance(value, str) and ',' in value:
                value = [item.strip() for item in value.split(',')]
                if arg_type != list:
                    value = [arg_type(item) for item in value]
            # Convertir booleanos
            elif arg_type == bool:
                if isinstance(value, str):
                    value = value.lower() in ('true', 't', 'yes', 'y', '1')
            # Convertir otros tipos
            else:
                value = arg_type(value)
                
            # Actualizar el valor en el diccionario
            values_dict[arg_name] = value
            
        except (ValueError, TypeError):
            # Si hay error en la conversión, dejar el valor original
            continue