def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    # Verificar que el comando existe
    if command_name not in self.commands:
        return []
        
    # Obtener el parser del comando
    parser = self.commands[command_name]
    
    # Lista para almacenar todas las opciones
    options = []
    
    # Recorrer todas las opciones del parser
    for action in parser._actions:
        # Obtener los nombres de la opción (corto y largo)
        option_strings = action.option_strings
        
        # Si no tiene strings de opción, continuar
        if not option_strings:
            continue
            
        # Crear diccionario con especificación de la opción
        option_spec = {
            'names': option_strings,
            'help': action.help,
            'required': action.required,
            'default': action.default,
            'type': action.type.__name__ if action.type else None,
            'choices': action.choices,
            'dest': action.dest
        }
        
        options.append(option_spec)
        
    return options