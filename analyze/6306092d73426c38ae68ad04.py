def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    if not hasattr(self, '_command_parser_specs'):
        self._command_parser_specs = {}

    if command_name in self._command_parser_specs:
        return self._command_parser_specs[command_name]
    
    # Aquí se asume que las especificaciones de las opciones se cargan de alguna fuente
    # Por ejemplo, un archivo de configuración o una base de datos
    # Este es un ejemplo de cómo podrían verse las especificaciones
    if command_name == "main":
        options = [
            {"name": "--verbose", "help": "Aumenta la verbosidad de la salida"},
            {"name": "--config", "help": "Especifica el archivo de configuración"}
        ]
    elif command_name == "virsh":
        options = [
            {"name": "--connect", "help": "Especifica la URI de conexión"},
            {"name": "--list", "help": "Lista todas las máquinas virtuales"}
        ]
    elif command_name == "ospd":
        options = [
            {"name": "--host", "help": "Especifica el host del servidor OSPD"},
            {"name": "--port", "help": "Especifica el puerto del servidor OSPD"}
        ]
    else:
        options = []

    self._command_parser_specs[command_name] = options
    return options