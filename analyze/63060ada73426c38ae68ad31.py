def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    # Obtener la configuración del parser
    parser_config = self.parsers_config.get(parser_name, {})
    
    # Iterar sobre los argumentos y convertir según el tipo definido
    for arg_name, value in values_dict.items():
        # Obtener la configuración del argumento específico
        arg_config = parser_config.get(arg_name, {})
        arg_type = arg_config.get('type', str)  # Por defecto es string
        
        # Saltar si el valor es None
        if value is None:
            continue
            
        try:
            # Manejar casos especiales
            if arg_type == bool:
                # Convertir strings a booleanos
                if isinstance(value, str):
                    value = value.lower()
                    values_dict[arg_name] = value in ('true', 't', 'yes', 'y', '1')
            elif arg_type == list:
                # Convertir string a lista
                if isinstance(value, str):
                    values_dict[arg_name] = value.split(',')
            else:
                # Convertir al tipo especificado
                values_dict[arg_name] = arg_type(value)
                
        except (ValueError, TypeError):
            # Si hay error en la conversión, mantener el valor original
            continue