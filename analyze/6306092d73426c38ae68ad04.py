def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    # Verificar que el comando existe
    if command_name not in self.parser_options:
        return []
        
    # Obtener todas las opciones para el comando
    options = []
    
    # Iterar sobre las opciones del comando
    for option in self.parser_options[command_name]:
        # Agregar cada opción a la lista
        options.append(option)
        
    return options