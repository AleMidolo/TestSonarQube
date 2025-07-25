def _convert_non_cli_args(self, parser_name, values_dict):
    """
    Convierte los argumentos a los tipos correctos modificando el parámetro values_dict.

    Por defecto, todos los valores son cadenas de texto (strings).

    :param parser_name: El nombre del comando, por ejemplo: main, virsh, ospd, etc.
    :param values_dict: El diccionario con los argumentos.
    """
    # Obtener la configuración del parser
    parser_config = self.config.get(parser_name, {})
    
    # Iterar sobre los argumentos
    for arg_name, value in values_dict.items():
        # Obtener el tipo definido en la configuración
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        # Convertir valores booleanos
        if arg_type == bool:
            if isinstance(value, str):
                values_dict[arg_name] = value.lower() in ('true', 't', 'yes', 'y', '1')
            continue
            
        # Convertir valores numéricos
        if arg_type in (int, float):
            try:
                values_dict[arg_name] = arg_type(value)
            except (ValueError, TypeError):
                continue
                
        # Convertir listas
        if arg_type == list:
            if isinstance(value, str):
                values_dict[arg_name] = [x.strip() for x in value.split(',') if x.strip()]
            continue
            
        # Convertir diccionarios
        if arg_type == dict:
            if isinstance(value, str):
                try:
                    import json
                    values_dict[arg_name] = json.loads(value)
                except json.JSONDecodeError:
                    continue