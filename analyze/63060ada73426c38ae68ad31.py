def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    # Obtener la configuración del parser
    parser_config = self.parsers_config.get(parser_name, {})
    
    # Iterar sobre los argumentos y convertirlos según su tipo
    for arg_name, value in values_dict.items():
        # Obtener la configuración del argumento específico
        arg_config = parser_config.get(arg_name, {})
        arg_type = arg_config.get('type', str)  # Por defecto es string
        
        # Saltar si el valor es None
        if value is None:
            continue
            
        try:
            # Convertir listas
            if isinstance(value, list):
                values_dict[arg_name] = [arg_type(item) for item in value]
            # Convertir valores booleanos
            elif arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
                else:
                    values_dict[arg_name] = bool(value)
            # Convertir otros tipos
            else:
                values_dict[arg_name] = arg_type(value)
                
        except (ValueError, TypeError):
            # Si hay error en la conversión, mantener el valor original
            continue