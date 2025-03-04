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
                # Si falla la conversión, mantener el valor original
                continue
                
        # Convertir listas
        if arg_type == list and isinstance(value, str):
            values_dict[arg_name] = value.split(',') if value else []
            
        # Convertir diccionarios
        if arg_type == dict and isinstance(value, str):
            try:
                import json
                values_dict[arg_name] = json.loads(value)
            except json.JSONDecodeError:
                # Si falla la conversión JSON, intentar convertir formato key=value,key2=value2
                try:
                    dict_items = [item.split('=') for item in value.split(',')]
                    values_dict[arg_name] = {k.strip(): v.strip() for k, v in dict_items}
                except:
                    # Si falla la conversión, mantener el valor original
                    continue